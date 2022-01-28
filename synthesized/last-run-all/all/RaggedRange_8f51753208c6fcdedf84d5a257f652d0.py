import tensorflow as tf

starts = tf.constant(-1879048192, shape=[], dtype=tf.int64)
limits = tf.constant(1, shape=[], dtype=tf.int64)
deltas = tf.constant(2, shape=[1], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=starts, limits=limits, deltas=deltas)