# SparseReorderOp

import tensorflow as tf

input_indices = tf.constant(0, shape=[2,2], dtype=tf.int64)
input_values = tf.constant([1,2], shape=[2], dtype=tf.float32)
input_shape = tf.constant([4,3], shape=[2], dtype=tf.int64)
tf.raw_ops.SparseReorder(input_indices=input_indices, input_values=input_values, input_shape=input_shape)
