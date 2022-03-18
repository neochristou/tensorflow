# Signal -11;2022-03-07 18:56:11.200563: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# SparseTensorDenseAddOp

import tensorflow as tf

a_indices = tf.constant(0, shape=[17,2], dtype=tf.int64)
a_values = tf.constant([], shape=[0], dtype=tf.float32)
a_shape = tf.constant([6,12], shape=[2], dtype=tf.int64)
b = tf.constant(-0.223668531, shape=[6,12], dtype=tf.float32)
tf.raw_ops.SparseTensorDenseAdd(a_indices=a_indices, a_values=a_values, a_shape=a_shape, b=b)