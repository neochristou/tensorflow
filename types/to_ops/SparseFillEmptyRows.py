# SparseFillEmptyRowsOp

import tensorflow as tf

indices = tf.constant([], shape=[0,2], dtype=tf.int64)
values = tf.constant([], shape=[0], dtype=tf.float64)
dense_shape = tf.constant([2,5], shape=[2], dtype=tf.int64)
default_value = tf.constant(-1, shape=[], dtype=tf.float64)
tf.raw_ops.SparseFillEmptyRows(indices=indices, values=values, dense_shape=dense_shape, default_value=default_value)
