# Signal -6;2022-01-20 07:06:05.726945: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:06:05.728948: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-20 07:06:05.733770: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Internal: Expected shape dimensions to be non-negative, got -1250999896764

import tensorflow as tf

arg_0 = tf.constant(0, shape=[1024000,2], dtype=tf.int64)
arg_1 = tf.constant(-3.5e+35, shape=[1024000], dtype=tf.float32)
arg_2 = tf.constant(-1250999896764, shape=[2], dtype=tf.int64)
arg_3 = tf.constant(8193, shape=[2], dtype=tf.int64)
arg_4 = tf.constant(8193, shape=[2], dtype=tf.int64)
tf.raw_ops.SparseSlice(indices=arg_0, values=arg_1, shape=arg_2, start=arg_3, size=arg_4)