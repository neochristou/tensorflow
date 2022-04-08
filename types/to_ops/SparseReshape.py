# SparseReshapeOp

import tensorflow as tf

input_indices = tf.constant(12, shape=[26,1], dtype=tf.int64)
input_shape = tf.constant(40, shape=[1], dtype=tf.int64)
new_shape = tf.constant([8,5], shape=[2], dtype=tf.int64)
tf.raw_ops.SparseReshape(input_indices=input_indices, input_shape=input_shape, new_shape=new_shape)
