# RangeOp

import tensorflow as tf

start = tf.constant(-1879048192, shape=[10,19,22], dtype=tf.int32)
limit = tf.constant(1879048192, shape=[22,19,5,13], dtype=tf.int32)
delta = tf.constant(1879048192, shape=[22,19,5,13], dtype=tf.int32)
tf.raw_ops.Range(start=start, limit=limit, delta=delta)
