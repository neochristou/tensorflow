# RandomPoissonOp

import tensorflow as tf

seed = 87654321
seed2 = 1503137960
dtype = tf.int64
shape = tf.constant([], shape=[0], dtype=tf.int32)
rate = tf.constant(3.5e+35, shape=[], dtype=tf.float32)
tf.raw_ops.RandomPoissonV2(shape=shape, rate=rate, seed=seed, seed2=seed2, dtype=dtype)