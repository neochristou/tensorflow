# Signal -6;2022-03-26 16:54:29.157690: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-26 16:54:29.161376: F tensorflow/core/kernels/fractional_max_pool_op.cc:390] Check failed: input_backprop_index >= 0 && input_backprop_index < num_total_inputs Invalid input backprop index: -1, 91

# FractionalMaxPoolGradOp

import tensorflow as tf

overlapping = True
orig_input = tf.constant(.453409232, shape=[1,7,13,1], dtype=tf.float32)
orig_output = tf.constant(.453409232, shape=[1,7,13,1], dtype=tf.float32)
out_backprop = tf.constant(.453409232, shape=[1,7,13,1], dtype=tf.float32)
row_pooling_sequence = tf.constant(0, shape=[5], dtype=tf.int64)
col_pooling_sequence = tf.constant(0, shape=[5], dtype=tf.int64)
tf.raw_ops.FractionalMaxPoolGrad(orig_input=orig_input, orig_output=orig_output, out_backprop=out_backprop, row_pooling_sequence=row_pooling_sequence, col_pooling_sequence=col_pooling_sequence, overlapping=overlapping)