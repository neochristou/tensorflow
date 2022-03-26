# Signal -6;2022-03-26 16:57:25.261243: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-26 16:57:25.264984: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Internal: Expected shape dimensions to be non-negative, got -1250999896764

# SparseFillEmptyRowsOp

import tensorflow as tf

indices = tf.constant(0, shape=[2,2], dtype=tf.int64)
values = tf.constant([1,1], shape=[2], dtype=tf.float32)
dense_shape = tf.constant([-1250999896764,-1250999896764], shape=[2], dtype=tf.int64)
default_value = tf.constant(1, shape=[], dtype=tf.float32)
tf.raw_ops.SparseFillEmptyRows(indices=indices, values=values, dense_shape=dense_shape, default_value=default_value)