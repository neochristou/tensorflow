# RangeOp

import tensorflow as tf

start = tf.constant(-536870912, shape=[], dtype=tf.int32)
limit = tf.constant(1, shape=[], dtype=tf.int32)
delta = tf.constant(2, shape=[], dtype=tf.int32)
tf.raw_ops.Range(start=start, limit=limit, delta=delta)