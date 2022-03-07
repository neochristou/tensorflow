# FusedBatchNormOpV3

import tensorflow as tf

epsilon = 0.001
exponential_avg_factor = 1
data_format = "NCHW"
is_training = True
x = tf.constant(00, shape=[1,6,4,1], dtype=tf.float32)
scale = tf.constant([], shape=[0], dtype=tf.float32)
offset = tf.constant(1, shape=[6], dtype=tf.float32)
mean = tf.constant([], shape=[0], dtype=tf.float32)
variance = tf.constant(1, shape=[6], dtype=tf.float32)
tf.raw_ops.FusedBatchNormV3(x=x, scale=scale, offset=offset, mean=mean, variance=variance, epsilon=epsilon, exponential_avg_factor=exponential_avg_factor, data_format=data_format, is_training=is_training)