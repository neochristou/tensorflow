import tensorflow as tf

splits = tf.constant(0, shape=[6], dtype=tf.int64)
values = tf.constant([], shape=[0], dtype=tf.int32)
size = tf.constant(65534, shape=[], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.RaggedBincount(splits=splits, values=values, size=size, weights=weights)