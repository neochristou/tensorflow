# Signal -11;2022-03-26 16:57:24.219983: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# SparseCount

import tensorflow as tf

binary_output = False
minlength = 6
maxlength = 6
indices = tf.constant(-1879048192, shape=[5,2], dtype=tf.int64)
values = tf.constant(0, shape=[5], dtype=tf.int64)
dense_shape = tf.constant(0, shape=[5,2], dtype=tf.int64)
weights = tf.constant(0, shape=[5], dtype=tf.int64)
tf.raw_ops.SparseCountSparseOutput(indices=indices, values=values, dense_shape=dense_shape, weights=weights, binary_output=binary_output, minlength=minlength, maxlength=maxlength)