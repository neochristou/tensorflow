# RandomPoissonOp

import tensorflow as tf

seed = 87654321
seed2 = 12345
dtype = tf.half
shape = tf.constant(1000, shape=[1], dtype=tf.int32)
rate = tf.constant(1, shape=[], dtype=tf.float32)
tf.raw_ops.RandomPoissonV2(shape=shape, rate=rate, seed=seed, seed2=seed2, dtype=dtype)
