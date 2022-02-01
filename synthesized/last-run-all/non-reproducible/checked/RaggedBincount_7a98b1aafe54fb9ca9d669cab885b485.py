# 2022-01-31 21:30:33.754865: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

import tensorflow as tf

splits = tf.constant(0, shape=[6], dtype=tf.int64)
values = tf.constant([], shape=[0], dtype=tf.int32)
size = tf.constant(65534, shape=[], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.RaggedBincount(splits=splits, values=values, size=size, weights=weights)