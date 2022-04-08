# RaggedRangeOp

import tensorflow as tf

Tsplits = tf.int64
starts = tf.constant([1,6], shape=[2], dtype=tf.int64)
limits = tf.constant([5,11], shape=[2], dtype=tf.int64)
deltas = tf.constant(1, shape=[], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=starts, limits=limits, deltas=deltas, Tsplits=Tsplits)
