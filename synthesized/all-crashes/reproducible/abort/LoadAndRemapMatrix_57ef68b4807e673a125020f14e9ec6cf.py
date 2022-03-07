# Signal -6;2022-03-04 18:44:49.369967: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:44:49.372531: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (1 vs. 0)Asking for tensor of 1 dimensions from a tensor of 0 dimensions

# LoadAndRemapMatrixOp

import tensorflow as tf

num_rows = 3
num_cols = 2
max_rows_in_memory = -1
ckpt_path = tf.constant("/tmp/warm_starting_util_testbdiyt3ov/tmp0qqyxz7g/model-0", shape=[], dtype=tf.string)
old_tensor_name = tf.constant("/tmp/warm_starting_util_testbdiyt3ov/tmp0qqyxz7g/model-0", shape=[], dtype=tf.string)
row_remapping = tf.constant(0, shape=[], dtype=tf.int64)
col_remapping = tf.constant(3, shape=[3], dtype=tf.int64)
initializing_values = tf.constant([], shape=[0,1], dtype=tf.float32)
tf.raw_ops.LoadAndRemapMatrix(ckpt_path=ckpt_path, old_tensor_name=old_tensor_name, row_remapping=row_remapping, col_remapping=col_remapping, initializing_values=initializing_values, num_rows=num_rows, num_cols=num_cols, max_rows_in_memory=max_rows_in_memory)