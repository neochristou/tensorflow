# Conv2DOp

import tensorflow as tf

strides = [1, 1, 1, 1]
padding = "SAME"
use_cudnn_on_gpu = True
explicit_paddings = []
data_format = "NHWC"
dilations = [1, 1, 1, 1]
input = tf.constant(0.430845976, shape=[1,2,2,5], dtype=tf.float32)
filter = tf.constant(-0.081049, shape=[5,5,5,5], dtype=tf.float32)
tf.raw_ops.Conv2D(input=input, filter=filter, strides=strides, padding=padding, use_cudnn_on_gpu=use_cudnn_on_gpu, explicit_paddings=explicit_paddings, data_format=data_format, dilations=dilations)
