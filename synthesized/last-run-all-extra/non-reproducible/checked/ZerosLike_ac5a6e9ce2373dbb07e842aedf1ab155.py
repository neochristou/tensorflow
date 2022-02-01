# No crash
# 2022-01-31 11:00:46.488801: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

import tensorflow as tf

x = tf.constant(3.5e+35, shape=[12, 18, 22, 19], dtype=tf.float32)
tf.raw_ops.ZerosLike(x=x)
