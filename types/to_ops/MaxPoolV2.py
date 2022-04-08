# MaxPoolingV2Op

import tensorflow as tf

padding = "SAME"
data_format = "NHWC"
input = tf.constant(1, shape=[1,1,1,10], dtype=tf.float32)
ksize = tf.constant(1, shape=[4], dtype=tf.int32)
strides = tf.constant(1, shape=[4], dtype=tf.int32)
tf.raw_ops.MaxPoolV2(input=input, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
