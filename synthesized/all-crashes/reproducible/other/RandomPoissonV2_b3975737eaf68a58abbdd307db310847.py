# Signal --4;2022-03-26 16:56:45.143524: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# RandomPoissonOp

import tensorflow as tf

seed = 87654321
seed2 = 1503137960
dtype = tf.int64
shape = tf.constant([], shape=[0], dtype=tf.int32)
rate = tf.constant(3.5e+35, shape=[], dtype=tf.float32)
tf.raw_ops.RandomPoissonV2(shape=shape, rate=rate, seed=seed, seed2=seed2, dtype=dtype)