# AddSparseToTensorsMapOp

import tensorflow as tf

container = ""
shared_name = "a"
sparse_indices = tf.constant(0, shape=[6,2], dtype=tf.int64)
sparse_values = tf.constant(0, shape=[6], dtype=tf.int32)
sparse_shape = tf.constant([3,4], shape=[2], dtype=tf.int64)
tf.raw_ops.AddSparseToTensorsMap(sparse_indices=sparse_indices, sparse_values=sparse_values, sparse_shape=sparse_shape, container=container, shared_name=shared_name)
