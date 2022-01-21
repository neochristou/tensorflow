import tensorflow as tf

arg_0 = tf.constant(0, shape=[4], dtype=tf.int32)
arg_1 = tf.constant(536870912, shape=[], dtype=tf.int32)
arg_2 = tf.constant([], shape=[0], dtype=tf.int64)
tf.raw_ops.Bincount(arr=arg_0, size=arg_1, weights=arg_2)