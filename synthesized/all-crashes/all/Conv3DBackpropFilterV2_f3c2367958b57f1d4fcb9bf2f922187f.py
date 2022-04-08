# Conv3DCustomBackpropFilterOp

import tensorflow as tf

strides = [1, 2, 2, 2, 1]
padding = "SAME"
data_format = "NDHWC"
dilations = [1, 1, 1, 1, 1]
input = tf.constant(1, shape=[2,6,8,6,2], dtype=tf.float32)
filter_sizes = tf.constant(0, shape=[], dtype=tf.int32)
out_backprop = tf.constant(1, shape=[2,6,8,6,2], dtype=tf.float32)
tf.raw_ops.Conv3DBackpropFilterV2(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop, strides=strides, padding=padding, data_format=data_format, dilations=dilations)
