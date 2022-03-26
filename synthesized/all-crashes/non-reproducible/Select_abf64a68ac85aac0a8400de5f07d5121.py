# 2022-03-26 16:57:18.122047: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# SelectOp

import tensorflow as tf

condition = tf.constant(False, shape=[], dtype=tf.bool)
x = tf.constant("[]", shape=[0], dtype=tf.string)
y = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.Select(condition=condition, x=x, y=y)