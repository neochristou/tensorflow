import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[1], dtype=tf.int64)
arg_1 = tf.constant(0, shape=[1], dtype=tf.int64)
arg_2 = tf.constant(3, shape=[1], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=arg_0, limits=arg_1, deltas=arg_2)