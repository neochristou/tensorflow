# SplitOpCPU

import tensorflow as tf

num_split = 3
axis = tf.constant(0, shape=[], dtype=tf.int32)
value = tf.constant(0.18463433217903202, shape=[6,5,7], dtype=tf.float64)
tf.raw_ops.Split(axis=axis, value=value, num_split=num_split)
