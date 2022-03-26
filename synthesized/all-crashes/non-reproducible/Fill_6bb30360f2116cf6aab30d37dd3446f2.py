# 2022-03-26 16:54:26.698266: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# FillOp

import tensorflow as tf

dims = tf.constant(536870912, shape=[], dtype=tf.int32)
value = tf.constant(-3.5e+35, shape=[], dtype=tf.float32)
tf.raw_ops.Fill(dims=dims, value=value)