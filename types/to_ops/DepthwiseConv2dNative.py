# DepthwiseConv2dNativeOp

import tensorflow as tf

strides = [1, 1, 1, 1]
padding = "VALID"
explicit_paddings = []
data_format = "NHWC"
dilations = [1, 1, 1, 1]
input = tf.constant(1, shape=[1,2,3,2], dtype=tf.float32)
filter = tf.constant(1, shape=[2,2,2,2], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNative(input=input, filter=filter, strides=strides, padding=padding, explicit_paddings=explicit_paddings, data_format=data_format, dilations=dilations)
