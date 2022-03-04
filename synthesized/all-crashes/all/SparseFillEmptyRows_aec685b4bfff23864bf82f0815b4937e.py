import tensorflow as tf

indices = tf.constant(-1879048192, shape=[5], dtype=tf.int64)
values = tf.constant(0, shape=[], dtype=tf.int64)
dense_shape = tf.constant(1250999896764, shape=[19,22,10], dtype=tf.int64)
default_value = tf.constant(-8608480567731124087, shape=[], dtype=tf.int64)
tf.raw_ops.SparseFillEmptyRowsOp(indices=indices, values=values, dense_shape=dense_shape, default_value=default_value)