# Pooling3DOp

import tensorflow as tf

ksize = [1, 2, 2, 2, 1]
strides = [1, 2, 2, 2, 1]
padding = "SAME"
data_format = "NDHWC"
input = tf.constant(1, shape=[1,2,2,4,3], dtype=tf.float32)
tf.raw_ops.AvgPool3D(input=input, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
