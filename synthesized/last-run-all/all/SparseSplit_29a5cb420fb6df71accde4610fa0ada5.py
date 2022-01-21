import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[5,2], dtype=tf.int64)
arg_1 = tf.constant(1, shape=[], dtype=tf.int64)
arg_2 = tf.constant(2, shape=[5], dtype=tf.int32)
arg_3 = tf.constant(1, shape=[], dtype=tf.int64)
tf.raw_ops.SparseSplit(split_dim=arg_0, indices=arg_1, values=arg_2, shape=arg_3)