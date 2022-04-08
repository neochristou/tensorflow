# BroadcastToOp

import tensorflow as tf

input = tf.constant(-10.6911821, shape=[1,7], dtype=tf.float32)
shape = tf.constant([3,7], shape=[2], dtype=tf.int32)
tf.raw_ops.BroadcastTo(input=input, shape=shape)
