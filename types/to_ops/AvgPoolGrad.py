# AvgPoolingGradOp

import tensorflow as tf

ksize = [1, 1, 1, 1]
strides = [1, 1, 1, 1]
padding = "VALID"
data_format = "NHWC"
orig_input_shape = tf.constant(2, shape=[4], dtype=tf.int32)
grad = tf.constant(1, shape=[2,1,5,2], dtype=tf.float32)
tf.raw_ops.AvgPoolGrad(orig_input_shape=orig_input_shape, grad=grad, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
