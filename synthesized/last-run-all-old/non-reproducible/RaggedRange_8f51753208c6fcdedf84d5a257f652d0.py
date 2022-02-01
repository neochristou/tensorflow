# 2022-01-28 15:26:51.431607: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-28 15:26:51.433819: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 7516192776 exceeds 10% of free system memory.

import tensorflow as tf

starts = tf.constant(-1879048192, shape=[], dtype=tf.int64)
limits = tf.constant(1, shape=[], dtype=tf.int64)
deltas = tf.constant(2, shape=[1], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=starts, limits=limits, deltas=deltas)