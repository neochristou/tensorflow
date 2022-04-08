# DepthwiseConv2dNativeBackpropFilterOp

import tensorflow as tf

strides = [1, 1, 1, 1]
padding = "SAME"
explicit_paddings = []
data_format = "NHWC"
dilations = [1, 1, 1, 1]
input = tf.constant(0.184634328, shape=[4,5,5,48], dtype=tf.float32)
filter_sizes = tf.constant(1, shape=[4], dtype=tf.int32)
out_backprop = tf.constant(0.977082, shape=[4,5,5,96], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropFilter(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop, strides=strides, padding=padding, explicit_paddings=explicit_paddings, data_format=data_format, dilations=dilations)
