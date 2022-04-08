# AssertOp

import tensorflow as tf

summarize = 3
condition = tf.constant(True, shape=[], dtype=tf.bool)
data = tf.constant(3, shape=[], dtype=tf.float32)
tf.raw_ops.Assert(condition=condition, data=data, summarize=summarize)
