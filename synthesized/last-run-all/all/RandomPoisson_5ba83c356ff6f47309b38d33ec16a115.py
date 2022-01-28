import tensorflow as tf

shape = tf.constant(1000, shape=[1], dtype=tf.int32)
rate = tf.constant(3.5e+35, shape=[], dtype=tf.float32)
tf.raw_ops.RandomPoisson(shape=shape, rate=rate)