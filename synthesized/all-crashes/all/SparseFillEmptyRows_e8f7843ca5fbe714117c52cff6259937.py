# SparseFillEmptyRowsOp

import tensorflow as tf

indices = tf.constant(0, shape=[2,2], dtype=tf.int64)
values = tf.constant([1,1], shape=[2], dtype=tf.float32)
dense_shape = tf.constant([-1250999896764,-1250999896764], shape=[2], dtype=tf.int64)
default_value = tf.constant(1, shape=[], dtype=tf.float32)
tf.raw_ops.SparseFillEmptyRows(indices=indices, values=values, dense_shape=dense_shape, default_value=default_value)
