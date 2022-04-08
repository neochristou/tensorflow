# AvgPoolingOp

import tensorflow as tf

ksize = [1, 1, 1, 1]
strides = [1, 1, 1, 1]
padding = "SAME"
data_format = "NHWC"
value = tf.constant(-1, shape=[2,1,5,2], dtype=tf.float32)
tf.raw_ops.AvgPool(value=value, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
