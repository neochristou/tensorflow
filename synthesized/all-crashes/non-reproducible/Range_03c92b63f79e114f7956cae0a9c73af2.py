# 2022-01-20 07:05:25.664531: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:05:25.666549: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[], dtype=tf.int32)
arg_1 = tf.constant(0, shape=[], dtype=tf.int32)
arg_2 = tf.constant(2, shape=[], dtype=tf.int32)
tf.raw_ops.Range(start=arg_0, limit=arg_1, delta=arg_2)