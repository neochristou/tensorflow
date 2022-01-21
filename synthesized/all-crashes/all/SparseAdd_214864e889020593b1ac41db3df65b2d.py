import tensorflow as tf

arg_0 = tf.constant(0, shape=[2,2], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float64)
arg_2 = tf.constant([], shape=[0], dtype=tf.int64)
arg_3 = tf.constant(-1879048192, shape=[2,2], dtype=tf.int64)
arg_4 = tf.constant(1, shape=[2], dtype=tf.int32)
arg_5 = tf.constant(0, shape=[2,2], dtype=tf.int64)
arg_6 = tf.constant(1, shape=[2], dtype=tf.int32)
tf.raw_ops.SparseAdd(a_indices=arg_0, a_values=arg_1, a_shape=arg_2, b_indices=arg_3, b_values=arg_4, b_shape=arg_5, thresh=arg_6)