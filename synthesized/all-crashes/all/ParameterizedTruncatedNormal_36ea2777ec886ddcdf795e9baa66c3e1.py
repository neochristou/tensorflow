import tensorflow as tf

arg_0 = tf.constant(100000, shape=[1], dtype=tf.int32)
arg_1 = tf.constant(0, shape=[], dtype=tf.float32)
arg_2 = tf.constant(-3.5e+35, shape=[], dtype=tf.float32)
arg_3 = tf.constant(0, shape=[], dtype=tf.float32)
arg_4 = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.ParameterizedTruncatedNormal(shape=arg_0, means=arg_1, stdevs=arg_2, minvals=arg_3, maxvals=arg_4)