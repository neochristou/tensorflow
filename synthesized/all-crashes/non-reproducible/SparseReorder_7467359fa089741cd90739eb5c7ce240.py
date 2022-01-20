# 2022-01-20 07:05:55.712688: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:05:55.714909: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[5,3], dtype=tf.int64)
arg_1 = tf.constant(3, shape=[5], dtype=tf.float32)
arg_2 = tf.constant(-1250999896764, shape=[3], dtype=tf.int64)
tf.raw_ops.SparseReorder(input_indices=arg_0, input_values=arg_1, input_shape=arg_2)