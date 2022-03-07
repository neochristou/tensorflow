# DepthwiseConv2dNativeBackpropFilterOp

import tensorflow as tf

strides = [1, 1, 1, 1]
padding = "SAME"
explicit_paddings = []
data_format = "NHWC"
dilations = [1, 1, 1, 1]
input = tf.constant(1, shape=[1,4,4,3], dtype=tf.float32)
filter_sizes = tf.constant(1879048192, shape=[13], dtype=tf.int32)
out_backprop = tf.constant(1, shape=[1,4,4,3], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropFilter(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop, strides=strides, padding=padding, explicit_paddings=explicit_paddings, data_format=data_format, dilations=dilations)