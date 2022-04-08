# GatherOp

import tensorflow as tf

batch_dims = 0
params = tf.constant(0, shape=[2,2], dtype=tf.int64)
indices = tf.constant([1,0], shape=[2], dtype=tf.int64)
axis = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.GatherV2(params=params, indices=indices, axis=axis, batch_dims=batch_dims)
