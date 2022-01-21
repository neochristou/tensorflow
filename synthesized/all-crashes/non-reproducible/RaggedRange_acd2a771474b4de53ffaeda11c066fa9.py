# 2022-01-20 07:05:08.281810: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:05:08.283850: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[1], dtype=tf.int64)
arg_1 = tf.constant(0, shape=[1], dtype=tf.int64)
arg_2 = tf.constant(3, shape=[1], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=arg_0, limits=arg_1, deltas=arg_2)