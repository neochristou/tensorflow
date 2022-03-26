# Signal -6;2022-03-26 16:54:28.124723: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-26 16:54:28.128410: F tensorflow/core/framework/tensor_shape.cc:397] Check failed: size >= 0 (-1879048192 vs. 0)

# FractionalAvgPoolGradOp

import tensorflow as tf

overlapping = True
orig_input_tensor_shape = tf.constant(-1879048192, shape=[4], dtype=tf.int64)
out_backprop = tf.constant([], shape=[0], dtype=tf.float64)
row_pooling_sequence = tf.constant(1, shape=[4], dtype=tf.int64)
col_pooling_sequence = tf.constant(1, shape=[4], dtype=tf.int64)
tf.raw_ops.FractionalAvgPoolGrad(orig_input_tensor_shape=orig_input_tensor_shape, out_backprop=out_backprop, row_pooling_sequence=row_pooling_sequence, col_pooling_sequence=col_pooling_sequence, overlapping=overlapping)