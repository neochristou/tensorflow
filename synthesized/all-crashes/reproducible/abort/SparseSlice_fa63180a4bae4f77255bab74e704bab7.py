# Signal -6;2022-04-07 20:03:10.384922: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:10.387285: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:03:10.388693: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Internal: Expected shape dimensions to be non-negative, got -1250999896764

# SparseSliceOp

import tensorflow as tf

indices = tf.constant(0, shape=[14,2], dtype=tf.int64)
values = tf.constant(0, shape=[14], dtype=tf.float32)
shape = tf.constant([-1250999896764,-1250999896764], shape=[2], dtype=tf.int64)
start = tf.constant([4,6], shape=[2], dtype=tf.int64)
size = tf.constant([4,6], shape=[2], dtype=tf.int64)
tf.raw_ops.SparseSlice(indices=indices, values=values, shape=shape, start=start, size=size)
