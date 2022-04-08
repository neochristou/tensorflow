# ReductionOp

import tensorflow as tf

keep_dims = False
input = tf.constant(0, shape=[14,12,12,5], dtype=tf.float32)
axis = tf.constant(0, shape=[4], dtype=tf.int32)
tf.raw_ops.Min(input=input, axis=axis, keep_dims=keep_dims)
