# ReduceJoinOp

import tensorflow as tf

keep_dims = True
separator = ""
inputs = tf.constant("[foo,bar]", shape=[2], dtype=tf.string)
reduction_indices = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.ReduceJoin(inputs=inputs, reduction_indices=reduction_indices, keep_dims=keep_dims, separator=separator)
