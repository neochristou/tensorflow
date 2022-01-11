import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[3], dtype=tf.int64)
arg_1 = tf.constant(1, shape=[3], dtype=tf.int64)
arg_2 = tf.constant(-1, shape=[3], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=arg_0, limits=arg_1, deltas=arg_2)