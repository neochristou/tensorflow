# Signal -11;2022-04-07 20:03:12.463054: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:12.465267: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# SparseTensorDenseAddOp

import tensorflow as tf

a_indices = tf.constant(0, shape=[17,2], dtype=tf.int64)
a_values = tf.constant([], shape=[0], dtype=tf.float32)
a_shape = tf.constant([6,12], shape=[2], dtype=tf.int64)
b = tf.constant(-0.223668531, shape=[6,12], dtype=tf.float32)
tf.raw_ops.SparseTensorDenseAdd(a_indices=a_indices, a_values=a_values, a_shape=a_shape, b=b)
