# AvgPooling3dGradOp

import tensorflow as tf

ksize = [1, 1, 1, 1, 1]
strides = [1, 1, 1, 1, 1]
padding = "VALID"
data_format = "NDHWC"
orig_input_shape = tf.constant(-536870912, shape=[5], dtype=tf.int32)
grad = tf.constant(100, shape=[1,3,5,4,1], dtype=tf.float32)
tf.raw_ops.AvgPool3DGrad(orig_input_shape=orig_input_shape, grad=grad, ksize=ksize, strides=strides, padding=padding, data_format=data_format)