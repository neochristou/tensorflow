# 2022-02-15 18:04:12.864770: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

import tensorflow as tf

start = tf.constant(-536870912, shape=[], dtype=tf.int32)
limit = tf.constant(1, shape=[], dtype=tf.int32)
delta = tf.constant(2, shape=[], dtype=tf.int32)
tf.raw_ops.Range(start=start, limit=limit, delta=delta)