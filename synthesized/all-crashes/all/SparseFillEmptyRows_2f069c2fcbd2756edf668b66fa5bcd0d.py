import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[6,2], dtype=tf.int64)
arg_1 = tf.constant(0, shape=[6], dtype=tf.float64)
arg_2 = tf.constant(-1250999896764, shape=[2], dtype=tf.int64)
arg_3 = tf.constant(-1, shape=[], dtype=tf.float64)
tf.raw_ops.SparseFillEmptyRows(indices=arg_0, values=arg_1, dense_shape=arg_2, default_value=arg_3)