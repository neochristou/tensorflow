# Conv2DCustomBackpropFilterOp

import tensorflow as tf

strides = [1, 1, 1, 1]
padding = "SAME"
use_cudnn_on_gpu = True
explicit_paddings = []
data_format = "NHWC"
dilations = [1, 1, 1, 1]
input = tf.constant(9.56056404, shape=[1,2,2,5], dtype=tf.float32)
filter_sizes = tf.constant(5, shape=[4], dtype=tf.int32)
out_backprop = tf.constant(0.1, shape=[1,2,2,5], dtype=tf.float32)
tf.raw_ops.Conv2DBackpropFilter(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop, strides=strides, padding=padding, use_cudnn_on_gpu=use_cudnn_on_gpu, explicit_paddings=explicit_paddings, data_format=data_format, dilations=dilations)
