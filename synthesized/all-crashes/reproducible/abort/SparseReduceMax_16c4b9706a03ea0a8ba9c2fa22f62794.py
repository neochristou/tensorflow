# Signal -6;2022-03-07 18:56:07.118162: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-07 18:56:07.120472: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Internal: Expected shape dimensions to be non-negative, got -1250999896764

# SparseReduceOp

import tensorflow as tf

keep_dims = False
input_indices = tf.constant(0, shape=[2,2], dtype=tf.int64)
input_values = tf.constant([1,2], shape=[2], dtype=tf.float32)
input_shape = tf.constant([-1250999896764,-1250999896764], shape=[2], dtype=tf.int64)
reduction_axes = tf.constant([0,1], shape=[2], dtype=tf.int32)
tf.raw_ops.SparseReduceMax(input_indices=input_indices, input_values=input_values, input_shape=input_shape, reduction_axes=reduction_axes, keep_dims=keep_dims)