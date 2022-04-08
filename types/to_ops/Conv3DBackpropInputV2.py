# Conv3DCustomBackpropInputOp

import tensorflow as tf

strides = [1, 1, 1, 1, 1]
padding = "VALID"
data_format = "NDHWC"
dilations = [1, 1, 1, 1, 1]
input_sizes = tf.constant(2, shape=[5], dtype=tf.int32)
filter = tf.constant(0, shape=[5,4,3,2,3], dtype=tf.float64)
out_backprop = tf.constant(1, shape=[2,1,1,1,3], dtype=tf.float64)
tf.raw_ops.Conv3DBackpropInputV2(input_sizes=input_sizes, filter=filter, out_backprop=out_backprop, strides=strides, padding=padding, data_format=data_format, dilations=dilations)
