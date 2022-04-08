# SparseBincountOp

import tensorflow as tf

binary_output = True
indices = tf.constant(102, shape=[4096], dtype=tf.int64)
values = tf.constant(0, shape=[4096], dtype=tf.int32)
dense_shape = tf.constant(128, shape=[1], dtype=tf.int64)
size = tf.constant(10, shape=[], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.float32)
tf.raw_ops.SparseBincount(indices=indices, values=values, dense_shape=dense_shape, size=size, weights=weights, binary_output=binary_output)
