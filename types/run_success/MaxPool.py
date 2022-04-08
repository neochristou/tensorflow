# MaxPoolingOp

import tensorflow as tf

ksize = [1, 1, 1, 1]
strides = [1, 1, 1, 1]
padding = "SAME"
explicit_paddings = []
data_format = "NHWC"
input = tf.constant(-1, shape=[2,1,5,2], dtype=tf.float32)
tf.raw_ops.MaxPool(input=input, ksize=ksize, strides=strides, padding=padding, explicit_paddings=explicit_paddings, data_format=data_format)
