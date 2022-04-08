# Conv3DOp

import tensorflow as tf

strides = [1, 1, 1, 1, 1]
padding = "VALID"
data_format = "NDHWC"
dilations = [1, 1, 1, 1, 1]
input = tf.constant(3.81469727e-06, shape=[8,16,16,16,8], dtype=tf.float32)
filter = tf.constant(0.015625, shape=[1,1,1,8,8], dtype=tf.float32)
tf.raw_ops.Conv3D(input=input, filter=filter, strides=strides, padding=padding, data_format=data_format, dilations=dilations)
