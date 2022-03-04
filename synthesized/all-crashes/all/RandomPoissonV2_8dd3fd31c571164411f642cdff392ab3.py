import tensorflow as tf

shape = tf.constant([], shape=[0], dtype=tf.int32)
rate = tf.constant(3.5e+35, shape=[], dtype=tf.float32)
tf.raw_ops.RandomPoissonV2(shape=shape, rate=rate)