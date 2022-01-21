import tensorflow as tf

arg_0 = tf.constant(0, shape=[1], dtype=tf.int32)
arg_1 = tf.constant(3.5e+35, shape=[], dtype=tf.float32)
tf.raw_ops.RandomPoisson(shape=arg_0, rate=arg_1)