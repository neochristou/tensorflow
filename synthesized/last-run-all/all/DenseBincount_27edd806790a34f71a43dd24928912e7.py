import tensorflow as tf

input = tf.constant(123, shape=[8,1], dtype=tf.int64)
size = tf.constant(123, shape=[8,1], dtype=tf.int64)
weights = tf.constant([], shape=[0], dtype=tf.float32)
tf.raw_ops.DenseBincount(input=input, size=size, weights=weights)