# DenseBincountOp

import tensorflow as tf

binary_output = False
input = tf.constant(1, shape=[2,4], dtype=tf.int64)
size = tf.constant(1, shape=[2,4], dtype=tf.int64)
weights = tf.constant([], shape=[0], dtype=tf.float32)
tf.raw_ops.DenseBincount(input=input, size=size, weights=weights, binary_output=binary_output)
