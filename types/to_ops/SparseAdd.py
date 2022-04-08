# SparseAddOp

import tensorflow as tf

a_indices = tf.constant(0, shape=[2,2], dtype=tf.int64)
a_values = tf.constant([1,2], shape=[2], dtype=tf.int32)
a_shape = tf.constant([3,4], shape=[2], dtype=tf.int64)
b_indices = tf.constant(0, shape=[2,2], dtype=tf.int64)
b_values = tf.constant([2,3], shape=[2], dtype=tf.int32)
b_shape = tf.constant([3,4], shape=[2], dtype=tf.int64)
thresh = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.SparseAdd(a_indices=a_indices, a_values=a_values, a_shape=a_shape, b_indices=b_indices, b_values=b_values, b_shape=b_shape, thresh=thresh)
