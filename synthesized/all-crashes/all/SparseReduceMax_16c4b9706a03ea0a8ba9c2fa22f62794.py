# SparseReduceOp

import tensorflow as tf

keep_dims = False
input_indices = tf.constant(0, shape=[2,2], dtype=tf.int64)
input_values = tf.constant([1,2], shape=[2], dtype=tf.float32)
input_shape = tf.constant([-1250999896764,-1250999896764], shape=[2], dtype=tf.int64)
reduction_axes = tf.constant([0,1], shape=[2], dtype=tf.int32)
tf.raw_ops.SparseReduceMax(input_indices=input_indices, input_values=input_values, input_shape=input_shape, reduction_axes=reduction_axes, keep_dims=keep_dims)
