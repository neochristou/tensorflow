import argparse
import glob
import hashlib
import inspect
import os

# import tensorflow as tf
from tensorflow import raw_ops

tf_path = "/media/ivysyn/tensorflow/"
#CRASHFILES_PATH = tf_path + "crashes/"
CRASHFILES_PATH = "/media/tf-fuzzing/results/"
REPRODUCE_PATH_BASE = tf_path + "synthesized/"
CRASH_DELIM = '--------------------------------------\n'


def get_tensor_type(dtype):
    if dtype == 'DT_FLOAT':
        return 'tf.float32'
    if dtype == 'DT_DOUBLE':
        return 'tf.float64'
    return dtype.replace('DT_', 'tf.').lower()


def get_tf_type(ttype):
    if ttype == 'half':
        return 'float16'
    if ttype == 'float':
        return 'float32'
    if ttype == 'double':
        return 'float64'
    return ttype


def get_op_name(logged_name, kernel_name):
    op_name = logged_name.split('/')[-1]
    try:
        eval(f"raw_ops.{op_name}")
        return op_name
    except AttributeError:
        return kernel_name[:-2]


def get_function_param_names(op_name):
    raw_op_fn = eval(f"raw_ops.{op_name}")
    params = inspect.signature(raw_op_fn).parameters.values()
    param_names = [param.name for param in params]
    return param_names


def handle_value_edge_cases(value):
    """Handle bad parsing"""

    value = value.replace('...', '')

    # Do negatives first, because of negative decimals
    if value.count('-') > 1:
        value = '-' + value.split('-')[1]
        return value

    if value.count('.') > 1:
        value = '.' + value.split('.')[1]

    if value[0] == '0' and '.' not in value and len(value) > 1:
        value = value[1:]

    return value


def parse_crash_argument(arg):

    attrs = arg.split(':')

    # This usually means unknown type (e.g., 'Resource' or 'Variant')
    # which is not printed as expected
    if len(attrs) < 3:
        return None

    tensor_type = attrs[1].replace(' shape', '').strip(' ')
    tensor_shape = attrs[2].replace(' values', '').strip(' ')

    tensor_values = attrs[3].strip('>').replace(
        '[', '').replace(']', '').split(' ')

    tensor_values = list(filter(None, tensor_values))
    return tensor_type, tensor_shape, tensor_values


def split_attrs(attrs):

    if len(attrs) == 0:
        return []

    parsed_attrs = []
    attrs = attrs.split(', ')

    idx = 0
    for attr in attrs:

        if '=' in attr:
            parsed_attrs.append(attr)
            idx += 1
        else:
            parsed_attrs[idx - 1] += ', ' + attr

    return parsed_attrs


def parse_attrs(attrs):

    attrs = split_attrs(attrs)
    attrs_dict = {}

    for attr in attrs:
        attr = attr.split('=')
        attr_name = attr[0]
        attr_value = attr[1]

        if attr_name in ('dtype', 'index_type', 'output_dtype', 'out_type', 'Tsplits'):
            attr_value = get_tensor_type(attr_value)

        if attr_name in ('dtypes',):
            attr_values = attr_value[1:-1].split(', ')
            attr_value = '[' + ', '.join(get_tensor_type(x)
                                         for x in attr_values) + ']'

        if attr_value == 'true':
            attr_value = 'True'
        if attr_value == 'false':
            attr_value = 'False'

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

        if param_name == 'name':
            break

        crash_args = parse_crash_argument(arg)

        # Will return none if it finds an arg in an unexpected format
        if crash_args is None:
            return None

        tensor_type, tensor_shape, tensor_values = crash_args

        if len(tensor_values) > 0:
            if tensor_shape == '[2]':
                print(tensor_values)
                value = '[' + ','.join(tensor_values) + ']'
            else:
                value = tensor_values[0]
                value = handle_value_edge_cases(value)
        else:
            value = '[]'

        if tensor_type == 'string':
            value = '"' + value + '"'

        if tensor_type == 'bool':
            if value == '0':
                value = 'False'
            else:
                value = 'True'

        fuzz_tensor = f"{param_name} = tf.constant({value}, shape={tensor_shape}, dtype=tf.{get_tf_type(tensor_type)})"
        input_args.append(fuzz_tensor)

    return input_args


def synthesize_file(crash, kernel_name):

    synth_file = []
    synth_file.append("# " + kernel_name + "\n")

    synth_file.append("import tensorflow as tf\n")

    crashing_args = crash.split('\n')
    op_name = get_op_name(crashing_args[0], kernel_name)
    attrs = parse_attrs(crashing_args[1])

    crashing_args = crashing_args[2:]
    if len(crashing_args) == 0:
        return -3, ''

    try:
        param_names = get_function_param_names(op_name)
    except AttributeError:
        # No raw op for this
        print(f"No raw op found for {kernel_name}, skipping")
        return -1, ''

    input_args = synthesize_args(crashing_args, param_names, attrs)

    if input_args is None:
        # Contains bad type
        # print(f"Bad type in {kernel_name}, skipping")
        return -2, ''

    synth_file.extend(input_args)

    kwargs = ["{}={}".format(param_names[idx], param_names[idx])
              for idx in range(len(input_args))]

    synth_file.append(f"tf.raw_ops.{op_name}({', '.join(kwargs)})")

    return '\n'.join(synth_file), op_name


def get_kernel_name(filename):
    crash_filename = filename.split('/')[-1]
    kernel_name = crash_filename.replace(
        CRASHFILES_PATH, '').replace('_crashes.log', '')
    return kernel_name


def save_synth_file(synth_file, op_name, reproduce_path):
    # Get the hash of the synthesized file to make sure we only
    # have unique reproduced files
    filehash = hashlib.md5(synth_file.encode()).hexdigest()
    out_filename = reproduce_path + op_name + '_' + filehash + '.py'

    # No duplicates
    if not os.path.isfile(out_filename):
        with open(out_filename, 'w') as f:
            f.write(synth_file)
            f.close()


def main():

    successful = set()
    all_kernels = set()
    no_raw_op = set()
    empty_crash_logs = set()
    bad_type = set()
    other_errors = set()

    args_parser = argparse.ArgumentParser(
        description="Parse and transform Pytorch native files")
    args_parser.add_argument(
        "--perf", dest="perf", action="store_true", default=False, help="Synth performance logs"
    )

    args = args_parser.parse_args()

    ext = '.duration' if args.perf else '*_crashes.log'
    reproduce_path = REPRODUCE_PATH_BASE
    if args.perf:
        reproduce_path += 'performance/'
    else:
        reproduce_path += 'all-crashes/'
    reproduce_path += 'all/'

    for crash_filename in glob.glob(CRASHFILES_PATH + ext):

        # Ignore empty files
        if os.path.getsize(crash_filename) == 0:
            continue

        kernel_name = get_kernel_name(crash_filename)

        with open(crash_filename, 'r') as crash_file:
            try:
                crashes = list(
                    filter(None, crash_file.read().split(CRASH_DELIM)))
            except UnicodeDecodeError:
                other_errors.add(kernel_name)
                continue

        all_kernels.add(kernel_name)

        for crash in crashes:
            crash = crash.strip()

            if len(crash) == 0:
                print("Skipping empty crash for", kernel_name)
                continue

            # print(kernel_name)
            synth_file, op_name = synthesize_file(crash, kernel_name)

            if synth_file is None:
                continue
            if synth_file == -1:
                no_raw_op.add(kernel_name)
                continue
            if synth_file == -2:
                bad_type.add(kernel_name)
                continue
            if synth_file == -3:
                empty_crash_logs.add(kernel_name)
                continue

            successful.add(kernel_name)
            save_synth_file(synth_file, op_name, reproduce_path)

    no_raw_op = list([x for x in no_raw_op if x not in successful])
    bad_type = list([x for x in bad_type if x not in successful])
    print("No raw op:")
    print('\n'.join(no_raw_op))
    print("Bad Type:")
    print('\n'.join(bad_type))
    print(f"Total no raw op: {len(no_raw_op)}")
    print(f"Total bad Type: {len(bad_type)}")
    print(f"Total other errors: {len(other_errors)}")
    print(f"Total successful: {len(successful)}")
    print(f"Total crash files: {len(all_kernels)}")


if __name__ == "__main__":
    main()
