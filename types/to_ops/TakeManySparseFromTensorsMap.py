# TakeManySparseFromTensorsMapOp

import tensorflow as tf

dtype = tf.int32
container = ""
shared_name = "a"
sparse_handles = tf.constant([0,1], shape=[2], dtype=tf.int64)
tf.raw_ops.TakeManySparseFromTensorsMap(sparse_handles=sparse_handles, dtype=dtype, container=container, shared_name=shared_name)
