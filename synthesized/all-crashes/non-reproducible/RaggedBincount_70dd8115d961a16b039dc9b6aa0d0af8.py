# 2022-04-07 20:02:51.996579: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:51.998877: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# RaggedBincountOp

import tensorflow as tf

binary_output = True
splits = tf.constant(0, shape=[6], dtype=tf.int64)
values = tf.constant([], shape=[0], dtype=tf.int32)
size = tf.constant(65534, shape=[], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.RaggedBincount(splits=splits, values=values, size=size, weights=weights, binary_output=binary_output)
