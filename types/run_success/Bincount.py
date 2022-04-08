# BincountOp

import tensorflow as tf

arr = tf.constant(0, shape=[10], dtype=tf.int32)
size = tf.constant(6, shape=[], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.Bincount(arr=arr, size=size, weights=weights)
