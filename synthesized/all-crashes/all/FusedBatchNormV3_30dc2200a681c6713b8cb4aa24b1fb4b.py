import tensorflow as tf

x = tf.constant(000, shape=[1,6,4,1], dtype=tf.float32)
scale = tf.constant([], shape=[0], dtype=tf.float32)
offset = tf.constant(1, shape=[6], dtype=tf.float32)
mean = tf.constant([], shape=[0], dtype=tf.float32)
variance = tf.constant(1, shape=[6], dtype=tf.float32)
tf.raw_ops.FusedBatchNormOpV3(x=x, scale=scale, offset=offset, mean=mean, variance=variance)