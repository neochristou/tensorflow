# SparseToDense

import tensorflow as tf

validate_indices = True
sparse_indices = tf.constant(0, shape=[20,4], dtype=tf.int32)
output_shape = tf.constant(2, shape=[4], dtype=tf.int32)
sparse_values = tf.constant(2.41642356, shape=[20], dtype=tf.float32)
default_value = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.SparseToDense(sparse_indices=sparse_indices, output_shape=output_shape, sparse_values=sparse_values, default_value=default_value, validate_indices=validate_indices)
