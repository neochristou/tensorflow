# Wrong type
# 2022-01-31 11:00:34.236399: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-31 11:00:34.238714: W tensorflow/core/framework/op_kernel.cc:1692] OP_REQUIRES failed at spacetobatch_op.cc:219 : Invalid argument: padded_shape[0]=2 is not divisible by block_shape[0]=-1879048192Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/SpaceToBatchND_d6b5555b792d46ddbd41e34e3e8e08b9.py", line 6, in <module>    tf.raw_ops.SpaceToBatchND(input=input, block_shape=block_shape, paddings=paddings)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_array_ops.py", line 9799, in space_to_batch_nd    _ops.raise_from_not_ok_status(e, name)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: padded_shape[0]=2 is not divisible by block_shape[0]=-1879048192 [Op:SpaceToBatchND]

import tensorflow as tf

input = tf.constant(123, shape=[2, 2, 4, 1], dtype=tf.float32)
block_shape = tf.constant(-1879048192, shape=[2], dtype=tf.int64)
paddings = tf.constant(0, shape=[2, 2], dtype=tf.int32)
tf.raw_ops.SpaceToBatchND(
    input=input, block_shape=block_shape, paddings=paddings)
