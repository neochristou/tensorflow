# 2022-02-15 18:04:04.907044: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-02-15 18:04:04.910979: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 7516192768 exceeds 10% of free system memory.

import tensorflow as tf

indices = tf.constant(-1250999896764, shape=[], dtype=tf.int64)
depth = tf.constant(1879048192, shape=[], dtype=tf.int32)
on_value = tf.constant(1, shape=[], dtype=tf.float32)
off_value = tf.constant(1, shape=[], dtype=tf.float32)
tf.raw_ops.OneHot(indices=indices, depth=depth, on_value=on_value, off_value=off_value)