import argparse
import glob
import hashlib
import inspect
import os

# import tensorflow as tf
from tensorflow import raw_ops

TF_PATH = "/media/ivysyn/tensorflow/"
CRASHFILES_PATH = TF_PATH + "crashes/"
# CRASHFILES_PATH = "/media/tf-fuzzing/results/"
REPRODUCE_PATH_BASE = TF_PATH + "synthesized/"
KERNEL_REGS_FILE = TF_PATH + "fuzz-utils/kernel_regs.txt"
CRASH_DELIM = "--------------------------------------\n"
TYPES_PATH = TF_PATH + "types/"
RES_PATH = TYPES_PATH + "to_ops/"


def get_tensor_type(dtype):
    if dtype == "DT_FLOAT":
        return "tf.float32"
    if dtype == "DT_DOUBLE":
        return "tf.float64"
    return dtype.replace("DT_", "tf.").lower()


def get_tf_type(ttype):
    if ttype == "half":
        return "float16"
    if ttype == "float":
        return "float32"
    if ttype == "double":
        return "float64"
    return ttype


def get_function_param_names(op_name):
    raw_op_fn = eval(f"raw_ops.{op_name}")
    params = inspect.signature(raw_op_fn).parameters.values()
    param_names = [param.name for param in params]
    return param_names


def handle_value_edge_cases(value):
    """Handle bad parsing"""

    value = value.replace("...", "")

    # Do negatives first, because of negative decimals
    if value.count("-") > 1:
        value = "-" + value.split("-")[1]
        return value

    if value.count(".") > 1:
        value = "." + value.split(".")[1]

    if len(value) > 1 and value[0] == "0" and "." not in value:
        value = value[1:]

    return value


def parse_crash_argument(arg):
    attrs = arg.split(":")

    # This usually means unknown type (e.g., 'Resource' or 'Variant')
    # which is not printed as expected
    if len(attrs) < 3:
        return None

    tensor_type = attrs[1].replace(" shape", "").strip(" ")
    tensor_shape = attrs[2].replace(" values", "").strip(" ")
    tensor_values = attrs[3].strip(">").replace(
        "[", "").replace("]", "").split(" ")

    tensor_values = list(filter(None, tensor_values))
    return tensor_type, tensor_shape, tensor_values


def split_attrs(attrs):

    if len(attrs) == 0:
        return []

    parsed_attrs = []
    attrs = attrs.split(", ")

    idx = 0
    for attr in attrs:

        if "=" in attr:
            parsed_attrs.append(attr)
            idx += 1
        else:
            if len(parsed_attrs) > 0:
                parsed_attrs[idx - 1] += ", " + attr

    return parsed_attrs


def parse_attrs(attrs):

    attrs = split_attrs(attrs)
    attrs_dict = {}

    for attr in attrs:
        attr = attr.split("=")
        attr_name = attr[0]
        attr_value = attr[1]

        if attr_name in ("dtype", "dt", "index_type", "output_dtype", "out_type", ) or attr_name.startswith("T"):
            attr_value = get_tensor_type(attr_value)

        if attr_name in ("dtypes",):
            attr_values = attr_value[1:-1].split(", ")
            attr_value = "[" + ", ".join(get_tensor_type(x)
                                         for x in attr_values) + "]"

        if attr_value == "true":
            attr_value = "True"
        if attr_value == "false":
            attr_value = "False"

        attrs_dict[attr_name] = attr_value

    return attrs_dict


def synthesize_args(crashing_args, param_names, attrs):

    input_args = []

    # Create attrs, if any
    for param_name in param_names:
        if param_name in attrs:
            attr_str = f"{param_name} = {attrs[param_name]}"
            input_args.append(attr_str)

    param_names = [x for x in param_names if x not in attrs]

    for idx, arg in enumerate(crashing_args):

        if idx >= len(param_names):
            break

        param_name = param_names[idx]

        if param_name == "name":
            break

        crash_args = parse_crash_argument(arg)

        # Will return none if it finds an arg in an unexpected format
        if crash_args is None:
            return None

        tensor_type, tensor_shape, tensor_values = crash_args

        if len(tensor_values) > 0:
            if tensor_shape == "[2]":
                value = "[" + ",".join(tensor_values) + "]"
            else:
                value = tensor_values[0]
                value = handle_value_edge_cases(value)
        else:
            value = "[]"

        if tensor_type == "string":
            value = '"' + value + '"'

        if tensor_type == "bool":
            if value == "0":
                value = "False"
            else:
                value = "True"

        if tensor_type == "variant":
            return None

        fuzz_tensor = f"{param_name} = tf.constant({value}, shape={tensor_shape}, dtype=tf.{get_tf_type(tensor_type)})"
        input_args.append(fuzz_tensor)

    return input_args


def synthesize_file(crash, kernel_name, op_name):

    if op_name is None:
        print(f"No op name registered for {kernel_name}")
        return -1

    synth_file = []
    synth_file.append("# " + kernel_name + "\n")
    synth_file.append("import tensorflow as tf\n")

    crashing_args = crash.split("\n")
    attrs = parse_attrs(crashing_args[0])

    crashing_args = crashing_args[1:]

    if len(crashing_args) == 0:
        return -3

    try:
        param_names = get_function_param_names(op_name)
    except AttributeError:
        # No raw op for this
        print(f"No raw op found for {kernel_name}, skipping")
        return -1

    input_args = synthesize_args(crashing_args, param_names, attrs)

    if input_args is None:
        # Contains unsupported type
        # print(f"unsupported type in {kernel_name}, skipping")
        return -2

    synth_file.extend(input_args)

    kwargs = ["{}={}".format(param_names[idx], param_names[idx])
              for idx in range(len(input_args))]

    synth_file.append(f"tf.raw_ops.{op_name}({', '.join(kwargs)})")

    return "\n".join(synth_file)


def get_kernel_name(filename, ext):
    crash_filename = filename.split("/")[-1]
    kernel_name = crash_filename.replace(
        CRASHFILES_PATH, "").replace(ext, "")
    return kernel_name


def save_synth_file(synth_file, op_name, reproduce_path, gettypes=False):
    # Get the hash of the synthesized file to make sure we only
    # have unique reproduced files
    filehash = hashlib.md5(synth_file.encode()).hexdigest()
    out_filename = reproduce_path + op_name

    if not gettypes:
        out_filename += "_" + filehash

    out_filename += ".py"

    # No duplicates
    if not os.path.isfile(out_filename):
        with open(out_filename, "w") as f:
            f.write(synth_file + "\n")
            f.close()


def main():

    successful = set()
    empty = set()
    successful_ops = set()
    all_kernels = set()
    no_raw_op = set()
    empty_crash_logs = set()
    synth_failed = set()
    unsupported_type = set()
    other_errors = set()
    no_args = set()

    args_parser = argparse.ArgumentParser(
        description="Parse and transform Pytorch native files")
    args_parser.add_argument("--gettypes", dest="gettypes", action="store_true",
                             default=False)

    args = args_parser.parse_args()

    kernel_regs = {}
    with open(KERNEL_REGS_FILE, "r") as f:
        regs = f.read().strip().split("\n")
        for reg in regs:
            kernel_name, op_name = reg.split(" ")
            kernel_regs[kernel_name] = op_name

    ext = ".types" if args.gettypes else "_crashes.log"
    logged_files = glob.glob(
        TYPES_PATH + "*types") if args.gettypes else glob.glob(CRASHFILES_PATH + "*_crashes.log")

    if args.gettypes:
        reproduce_path = TYPES_PATH + "to_ops/"
    else:
        reproduce_path = REPRODUCE_PATH_BASE + "all-crashes/all/"

    for crash_filename in logged_files:

        kernel_name = get_kernel_name(crash_filename, ext)

        op_name = None
        if kernel_name in kernel_regs:
            op_name = kernel_regs[kernel_name]
        elif kernel_name.endswith("Base"):
            b_kernel_name = kernel_name.replace("Base", "")
            if b_kernel_name in kernel_regs:
                op_name = kernel_regs[b_kernel_name]

        all_kernels.add(kernel_name)

        # Ignore empty files
        if os.path.getsize(crash_filename) == 0:
            empty.add(kernel_name)
            continue

        with open(crash_filename, "r") as crash_file:
            try:
                crashes = list(
                    filter(None, crash_file.read().split(CRASH_DELIM)))
            except UnicodeDecodeError as e:
                other_errors.add(kernel_name)
                continue

        if len(crashes) == 0:
            empty.add(kernel_name)
            continue

        if len(crashes) == 1 and crashes[0] == '\n\n':
            empty.add(kernel_name)
            continue

        for crash in crashes:

            crash = crash.rstrip()

            if len(crash) == 0:
                print("Skipping empty crash for", kernel_name)
                continue

            synth_file = synthesize_file(crash, kernel_name, op_name)

            if synth_file is None:
                synth_failed.add(kernel_name)
                continue
            if synth_file == -1:
                no_raw_op.add(kernel_name)
                continue
            if synth_file == -2:
                unsupported_type.add(kernel_name)
                continue
            if synth_file == -3:
                no_args.add(kernel_name)
                continue

            successful.add(kernel_name)
            successful_ops.add(op_name)
            save_synth_file(synth_file, op_name, reproduce_path, args.gettypes)

    no_raw_op = list([x for x in no_raw_op if x not in successful])
    unsupported_type = list(
        [x for x in unsupported_type if x not in successful])
    print("No raw op:")
    print("\n".join(no_raw_op))
    print("unsupported type:")
    print("\n".join(unsupported_type))
    print(f"Total synth_failed: {len(synth_failed)}")
    print(f"Total no raw op: {len(no_raw_op)}")
    print(f"Total empty files: {len(empty)}")
    print(f"Total no args: {len(no_args)}")
    print(f"Total unsupported type: {len(unsupported_type)}")
    print(f"Total other errors: {len(other_errors)}")
    print(f"Total successful: {len(successful)}")
    print(f"Total crash files: {len(all_kernels)}")
    print(f"Total successful (unique ops): {len(successful_ops)}")

    print([x for x in all_kernels if x not in no_raw_op and x not in empty and x not in unsupported_type
           and x not in other_errors and x not in successful and x not in no_args])


if __name__ == "__main__":
    main()
