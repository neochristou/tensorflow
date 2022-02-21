import tensorflow as tf

starts = tf.constant(-1879048192, shape=[2], dtype=tf.int64)
limits = tf.constant(0, shape=[2], dtype=tf.int64)
deltas = tf.constant(0, shape=[2], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=starts, limits=limits, deltas=deltas)