# Conv2DCustomBackpropInputOp

import tensorflow as tf

strides = [1, 1, 1, 1]
padding = "SAME"
use_cudnn_on_gpu = True
explicit_paddings = []
data_format = "NHWC"
dilations = [1, 1, 1, 1]
input_sizes = tf.constant(14, shape=[4], dtype=tf.int32)
filter = tf.constant(-0.137709618, shape=[5,5,5,5], dtype=tf.float32)
out_backprop = tf.constant(-0, shape=[14,12,12,5], dtype=tf.float32)
tf.raw_ops.Conv2DBackpropInput(input_sizes=input_sizes, filter=filter, out_backprop=out_backprop, strides=strides, padding=padding, use_cudnn_on_gpu=use_cudnn_on_gpu, explicit_paddings=explicit_paddings, data_format=data_format, dilations=dilations)
