import tensorflow as tf

arg_0 = tf.constant(0, shape=[140,2], dtype=tf.int64)
arg_1 = tf.constant(60, shape=[2], dtype=tf.int64)
arg_2 = tf.constant(-1879048192, shape=[140], dtype=tf.int64)
arg_3 = tf.constant(0, shape=[], dtype=tf.int64)
tf.raw_ops.SparseFillEmptyRows(indices=arg_0, values=arg_1, dense_shape=arg_2, default_value=arg_3)