# Signal --4;2022-03-26 16:53:33.464773: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# AdjustHueOp

import tensorflow as tf

images = tf.constant(0, shape=[2,2,3], dtype=tf.float32)
delta = tf.constant(-3.5e+35, shape=[], dtype=tf.float32)
tf.raw_ops.AdjustHue(images=images, delta=delta)