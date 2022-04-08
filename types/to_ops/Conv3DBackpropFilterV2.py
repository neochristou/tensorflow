# Conv3DBackpropFilterOp

import tensorflow as tf

strides = [1, 1, 1, 1, 1]
padding = "VALID"
data_format = "NDHWC"
dilations = [1, 1, 1, 1, 1]
input = tf.constant(0, shape=[2,5,4,3,2], dtype=tf.float16)
filter_sizes = tf.constant(5, shape=[5], dtype=tf.int32)
out_backprop = tf.constant(1, shape=[2,1,1,1,3], dtype=tf.float16)
tf.raw_ops.Conv3DBackpropFilterV2(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop, strides=strides, padding=padding, data_format=data_format, dilations=dilations)
