# Signal -6;2022-04-07 20:03:11.439558: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:11.441778: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:03:11.443094: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Internal: Expected shape dimensions to be non-negative, got -1250999896764

# SparseSoftmaxOp

import tensorflow as tf

sp_indices = tf.constant(0, shape=[72,3], dtype=tf.int64)
sp_values = tf.constant(0.301107913, shape=[72], dtype=tf.float32)
sp_shape = tf.constant(-1250999896764, shape=[3], dtype=tf.int64)
tf.raw_ops.SparseSoftmax(sp_indices=sp_indices, sp_values=sp_values, sp_shape=sp_shape)
