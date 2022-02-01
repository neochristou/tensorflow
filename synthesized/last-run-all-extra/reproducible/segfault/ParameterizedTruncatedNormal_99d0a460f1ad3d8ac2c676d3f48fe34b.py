# Signal -11;2022-01-31 11:00:26.767554: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

import tensorflow as tf

shape = tf.constant(100000, shape=[1], dtype=tf.int32)
means = tf.constant(0, shape=[], dtype=tf.float32)
stdevs = tf.constant(0, shape=[], dtype=tf.float32)
minvals = tf.constant(0, shape=[], dtype=tf.float32)
maxvals = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.ParameterizedTruncatedNormal(shape=shape, means=means, stdevs=stdevs, minvals=minvals, maxvals=maxvals)