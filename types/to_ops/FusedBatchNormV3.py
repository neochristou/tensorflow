# FusedBatchNormOpV3

import tensorflow as tf

epsilon = 0.001
exponential_avg_factor = 0.1
data_format = "NHWC"
is_training = True
x = tf.constant(100.184631, shape=[10,4,4,3], dtype=tf.float32)
scale = tf.constant(0.987534046, shape=[3], dtype=tf.float32)
offset = tf.constant(0.00676002633, shape=[3], dtype=tf.float32)
mean = tf.constant(19.1041603, shape=[3], dtype=tf.float32)
variance = tf.constant(0.821198285, shape=[3], dtype=tf.float32)
tf.raw_ops.FusedBatchNormV3(x=x, scale=scale, offset=offset, mean=mean, variance=variance, epsilon=epsilon, exponential_avg_factor=exponential_avg_factor, data_format=data_format, is_training=is_training)
