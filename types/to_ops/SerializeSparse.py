# SerializeSparseOp

import tensorflow as tf

out_type = tf.variant
sparse_indices = tf.constant(0, shape=[2,2], dtype=tf.int64)
sparse_values = tf.constant([3,5], shape=[2], dtype=tf.float32)
sparse_shape = tf.constant([100,100], shape=[2], dtype=tf.int64)
tf.raw_ops.SerializeSparse(sparse_indices=sparse_indices, sparse_values=sparse_values, sparse_shape=sparse_shape, out_type=out_type)
