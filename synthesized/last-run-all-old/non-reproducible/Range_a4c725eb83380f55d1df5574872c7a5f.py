# 2022-01-28 15:26:58.521495: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-28 15:26:58.523460: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 15032385552 exceeds 10% of free system memory.

import tensorflow as tf

start = tf.constant(-1879048192, shape=[], dtype=tf.int64)
limit = tf.constant(2, shape=[], dtype=tf.int64)
delta = tf.constant(1, shape=[], dtype=tf.int64)
tf.raw_ops.Range(start=start, limit=limit, delta=delta)