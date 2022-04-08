# DepthwiseConv2dNativeBackpropInputOp

import tensorflow as tf

strides = [1, 1, 1, 1]
padding = "SAME"
explicit_paddings = []
data_format = "NHWC"
dilations = [1, 1, 1, 1]
input_sizes = tf.constant(1879048192, shape=[13], dtype=tf.int32)
filter = tf.constant(0.184634328, shape=[1,1,48,2], dtype=tf.float32)
out_backprop = tf.constant(0.184634328, shape=[1,1,48,2], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropInput(input_sizes=input_sizes, filter=filter, out_backprop=out_backprop, strides=strides, padding=padding, explicit_paddings=explicit_paddings, data_format=data_format, dilations=dilations)
