# FusedBatchNormGradOpV3

import tensorflow as tf

epsilon = 0.001
data_format = "NHWC"
is_training = True
y_backprop = tf.constant(-0.00853636581, shape=[10,4,4,3], dtype=tf.float32)
x = tf.constant(100.184631, shape=[10,4,4,3], dtype=tf.float32)
scale = tf.constant(1, shape=[3], dtype=tf.float32)
reserve_space_1 = tf.constant(100.487984, shape=[3], dtype=tf.float32)
reserve_space_2 = tf.constant(0.0821950883, shape=[3], dtype=tf.float32)
reserve_space_3 = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.FusedBatchNormGradV3(y_backprop=y_backprop, x=x, scale=scale, reserve_space_1=reserve_space_1, reserve_space_2=reserve_space_2, reserve_space_3=reserve_space_3, epsilon=epsilon, data_format=data_format, is_training=is_training)
