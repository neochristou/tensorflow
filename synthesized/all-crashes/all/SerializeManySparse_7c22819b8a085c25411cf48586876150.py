import tensorflow as tf

sparse_indices = tf.constant(0, shape=[3,2], dtype=tf.int64)
sparse_values = tf.constant(1879048192, shape=[], dtype=tf.int32)
sparse_shape = tf.constant([], shape=[0], dtype=tf.int64)
tf.raw_ops.SerializeManySparse(sparse_indices=sparse_indices, sparse_values=sparse_values, sparse_shape=sparse_shape)