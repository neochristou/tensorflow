import tensorflow as tf

arg_0 = tf.constant([], shape=[0,2], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float64)
arg_2 = tf.constant(-1250999896764, shape=[2], dtype=tf.int64)
arg_3 = tf.constant(-1, shape=[], dtype=tf.float64)
tf.raw_ops.SparseFillEmptyRows(indices=arg_0, values=arg_1, dense_shape=arg_2, default_value=arg_3)