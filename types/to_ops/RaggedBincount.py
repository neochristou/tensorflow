# RaggedBincountOp

import tensorflow as tf

binary_output = True
splits = tf.constant(0, shape=[6], dtype=tf.int64)
values = tf.constant(3, shape=[7], dtype=tf.int32)
size = tf.constant(6, shape=[], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.float32)
tf.raw_ops.RaggedBincount(splits=splits, values=values, size=size, weights=weights, binary_output=binary_output)
