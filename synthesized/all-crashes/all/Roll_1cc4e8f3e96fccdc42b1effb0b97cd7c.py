import tensorflow as tf

arg_0 = tf.constant(0, shape=[5], dtype=tf.float32)
arg_1 = tf.constant([], shape=[0], dtype=tf.float64)
arg_2 = tf.constant(3, shape=[], dtype=tf.int32)
tf.raw_ops.Roll(input=arg_0, shift=arg_1, axis=arg_2)