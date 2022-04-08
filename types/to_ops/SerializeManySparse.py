# SerializeManySparseOp

import tensorflow as tf

out_type = tf.string
sparse_indices = tf.constant(0, shape=[3,2], dtype=tf.int64)
sparse_values = tf.constant("a", shape=[3], dtype=tf.string)
sparse_shape = tf.constant([4,5], shape=[2], dtype=tf.int64)
tf.raw_ops.SerializeManySparse(sparse_indices=sparse_indices, sparse_values=sparse_values, sparse_shape=sparse_shape, out_type=out_type)
