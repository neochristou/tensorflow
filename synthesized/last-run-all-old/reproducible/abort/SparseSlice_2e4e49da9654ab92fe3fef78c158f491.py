# Signal -6;2022-01-28 15:27:07.095175: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-28 15:27:07.097450: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Internal: Expected shape dimensions to be non-negative, got -1250999896764

import tensorflow as tf

indices = tf.constant(0, shape=[6,2], dtype=tf.int64)
values = tf.constant([], shape=[0], dtype=tf.int32)
shape = tf.constant(-1250999896764, shape=[2], dtype=tf.int64)
start = tf.constant(4, shape=[2], dtype=tf.int64)
size = tf.constant(4, shape=[2], dtype=tf.int64)
tf.raw_ops.SparseSlice(indices=indices, values=values, shape=shape, start=start, size=size)