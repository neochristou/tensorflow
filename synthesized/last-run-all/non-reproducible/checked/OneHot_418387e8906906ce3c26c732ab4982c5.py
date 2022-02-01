# 2022-01-31 21:30:30.361476: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

import tensorflow as tf

indices = tf.constant(1250999896764, shape=[], dtype=tf.int64)
depth = tf.constant(536870912, shape=[], dtype=tf.int32)
on_value = tf.constant(1, shape=[], dtype=tf.float32)
off_value = tf.constant(1, shape=[], dtype=tf.float32)
tf.raw_ops.OneHot(indices=indices, depth=depth, on_value=on_value, off_value=off_value)