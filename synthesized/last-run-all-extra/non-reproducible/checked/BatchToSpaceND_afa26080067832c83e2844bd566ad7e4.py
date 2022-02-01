# Wrong type
# 2022-01-31 10:59:26.577975: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/BatchToSpaceND_afa26080067832c83e2844bd566ad7e4.py", line 6, in <module>    tf.raw_ops.BatchToSpaceND(input=input, block_shape=block_shape, crops=crops)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_array_ops.py", line 467, in batch_to_space_nd    _ops.raise_from_not_ok_status(e, name)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: crops should have shape [2, 2] instead of [] [Op:BatchToSpaceND]

import tensorflow as tf

input = tf.constant(0, shape=[20, 5, 8, 7], dtype=tf.float32)
block_shape = tf.constant(-1879048192, shape=[2], dtype=tf.int64)
crops = tf.constant(1250999896764, shape=[], dtype=tf.int64)
tf.raw_ops.BatchToSpaceND(input=input, block_shape=block_shape, crops=crops)
