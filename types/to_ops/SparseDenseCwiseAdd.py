# SparseDenseBinaryOpShared

import tensorflow as tf

sp_indices = tf.constant(0, shape=[2,2], dtype=tf.int64)
sp_values = tf.constant([1,1], shape=[2], dtype=tf.int32)
sp_shape = tf.constant([2,2], shape=[2], dtype=tf.int64)
dense = tf.constant(1, shape=[2,2], dtype=tf.int32)
tf.raw_ops.SparseDenseCwiseAdd(sp_indices=sp_indices, sp_values=sp_values, sp_shape=sp_shape, dense=dense)
