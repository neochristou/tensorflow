import glob
import hashlib
import inspect
import os

# import tensorflow as tf
from tensorflow import raw_ops

CRASHFILES_PATH = "/media/mlfuzz/tensorflow/crashes/"
REPRODUCE_PATH = "/media/fuzzing-pytorch/pytorch-reproduce-tests/tf/all-crashes/"
CRASH_DELIM = '--------------------------------------\n'


def get_tf_type(ttype):
    if ttype == 'half':
        return 'float16'
    if ttype == 'float':
        return 'float32'
    if ttype == 'double':
        return 'float64'
    return ttype


def get_function_param_names(kernel_name):
    raw_op_fn = eval(f"raw_ops.{kernel_name}")
    params = inspect.signature(raw_op_fn).parameters.values()
    param_names = [param.name for param in params]
    return param_names


def handle_value_edge_cases(value):
    "Handle bad parsing"

    value = value.replace('...', '')

    # Do negatives first, because of negative decimals
    if value.count('-') > 1:
        value = '-' + value.split('-')[1]
        return value

    if value.count('.') > 1:
        value = '.' + value.split('.')[1]

    return value


def parse_crash_argument(arg):
    attrs = arg.split(':')

    # This usually means unknown type (e.g., 'Resource' or 'Variant')
    # which is not printed as expected
    if len(args) < 3:
        return None

    tensor_type = attrs[1].replace(' shape', '').strip(' ')
    tensor_shape = attrs[2].replace(' values', '').strip(' ')
    # TODO get the actual values, for now we assume they are all the same
    tensor_values = attrs[3].strip('>').replace(
        '[', '').replace(']', '').split(' ')
    tensor_values = list(filter(None, tensor_values))
    return tensor_type, tensor_shape, tensor_values


def synthesize_args(crashing_args, param_names):
    fuzz_tensors = []
    for idx, arg in enumerate(crashing_args):
        # Sometimes native function (maybe) has more parameters than python function
        # If this is the case, just take the first crashing parameters
        # TODO can probably optimize, sometimes there are duplicates -- see SparceConcatOp
        if idx >= len(param_names):
            break

        param_name = param_names[idx]
        crash_args = parse_crash_argument(arg)

        # Will return none if it finds an arg in an unexpected format
        if crash_args is None:
            return None

        tensor_type, tensor_shape, tensor_values = crash_args

        if len(tensor_values) > 0:
            value = tensor_values[0]
            value = handle_value_edge_cases(value)
        else:
            value = '[]'

        if tensor_type == 'string':
            value = '"' + value + '"'

        fuzz_tensor = f"arg_{idx} = tf.constant({value}, shape={tensor_shape}, dtype=tf.{get_tf_type(tensor_type)})"
        fuzz_tensors.append(fuzz_tensor)

    return fuzz_tensors


def synthesize_file(crash, kernel_name):
    synth_file = []
    synth_file.append("import tensorflow as tf\n")

    crashing_args = crash.split('\n')
    try:
        param_names = get_function_param_names(kernel_name)
    except AttributeError as e:
        # No raw op for this
        print(f"No raw op found for {kernel_name}, skipping")
        return None

    fuzz_tensors = synthesize_args(crashing_args, param_names)

    if fuzz_tensors is None:
        # Contains bad type
        print(f"Bad type {kernel_name}, skipping")
        return None

    synth_file.extend(fuzz_tensors)

    kwargs = ["{}=arg_{}".format(param_names[idx], idx)
              for idx in range(len(fuzz_tensors))]

    synth_file.append(f"tf.raw_ops.{kernel_name}({', '.join(kwargs)})")

    # print('\n'.join(synth_file))
    return '\n'.join(synth_file)


def get_kernel_name(filename):
    crash_filename = filename.split('/')[-1]
    kernel_name = crash_filename.replace(
        CRASHFILES_PATH, '').replace('_crashes.log', '')
    if kernel_name.endswith('Op'):
        kernel_name = kernel_name.replace('Op', '')
    return kernel_name


def save_synth_file(synth_file, kernel_name):
    # Get the hash of the synthesized file to make sure we only
    # have unique reproduced files
    filehash = hashlib.md5(synth_file.encode()).hexdigest()
    out_filename = REPRODUCE_PATH + kernel_name + '_' + filehash + '.py'

    # No duplicates
    if not os.path.isfile(out_filename):
        with open(out_filename, 'w') as f:
            f.write(synth_file)
            f.close()


def main():
    for crash_dir in glob.glob(CRASHFILES_PATH + '/*/'):
        for crash_filename in glob.glob(crash_dir + '*_crashes.log'):

            crash_file = open(crash_filename, 'r')
            crashes = list(filter(None, crash_file.read().split(CRASH_DELIM)))
            crash_file.close()

            kernel_name = get_kernel_name(crash_filename)

            for crash in crashes:
                crash = crash.strip()

                if len(crash) == 0:
                    print("Skipping empty crash for", kernel_name)
                    continue

                # print(kernel_name)
                synth_file = synthesize_file(crash, kernel_name)
                if synth_file is not None:
                    save_synth_file(synth_file, kernel_name)


if __name__ == "__main__":
    main()
