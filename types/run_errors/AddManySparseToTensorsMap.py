# AddManySparseToTensorsMapOp

import tensorflow as tf

container = ""
shared_name = ""
sparse_indices = tf.constant(0, shape=[3,2], dtype=tf.int64)
sparse_values = tf.constant("a", shape=[3], dtype=tf.string)
sparse_shape = tf.constant([4,5], shape=[2], dtype=tf.int64)
tf.raw_ops.AddManySparseToTensorsMap(sparse_indices=sparse_indices, sparse_values=sparse_values, sparse_shape=sparse_shape, container=container, shared_name=shared_name)
