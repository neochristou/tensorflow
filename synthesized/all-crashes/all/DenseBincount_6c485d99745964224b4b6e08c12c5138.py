import tensorflow as tf

input = tf.constant(1, shape=[2,3], dtype=tf.int32)
size = tf.constant(1, shape=[2,3], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.float32)
tf.raw_ops.DenseBincountOp(input=input, size=size, weights=weights)