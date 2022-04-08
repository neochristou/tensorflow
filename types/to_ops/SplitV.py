# SplitVOpCPU

import tensorflow as tf

num_split = 1
value = tf.constant([], shape=[0,2], dtype=tf.complex128)
size_splits = tf.constant(0, shape=[1], dtype=tf.int32)
axis = tf.constant(-2, shape=[], dtype=tf.int32)
tf.raw_ops.SplitV(value=value, size_splits=size_splits, axis=axis, num_split=num_split)
