# Signal -6;2022-04-07 20:03:13.517421: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:13.519669: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:03:13.521157: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (2 vs. 1)Asking for tensor of 2 dimensions from a tensor of 1 dimensions

# SparseTensorToCSRSparseMatrixCPUOp

import tensorflow as tf

indices = tf.constant(53, shape=[3], dtype=tf.int64)
values = tf.constant(0.554979503, shape=[218650], dtype=tf.float32)
dense_shape = tf.constant(53, shape=[3], dtype=tf.int64)
tf.raw_ops.SparseTensorToCSRSparseMatrix(indices=indices, values=values, dense_shape=dense_shape)
