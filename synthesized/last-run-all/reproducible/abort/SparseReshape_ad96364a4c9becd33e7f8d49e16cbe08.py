# Signal -6;2022-01-31 21:30:42.237143: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-31 21:30:42.239709: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Internal: Expected shape dimensions to be non-negative, got -1879048192

import tensorflow as tf

input_indices = tf.constant([], shape=[0,1], dtype=tf.int64)
input_shape = tf.constant(-1879048192, shape=[1], dtype=tf.int64)
new_shape = tf.constant(0, shape=[1], dtype=tf.int64)
tf.raw_ops.SparseReshape(input_indices=input_indices, input_shape=input_shape, new_shape=new_shape)