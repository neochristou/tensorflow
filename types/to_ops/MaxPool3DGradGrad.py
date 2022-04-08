# MaxPooling3dGradGradOp

import tensorflow as tf

ksize = [1, 1, 1, 1, 1]
strides = [1, 1, 1, 1, 1]
padding = "SAME"
data_format = "NDHWC"
orig_input = tf.constant(123, shape=[1,3,2,4,1], dtype=tf.float32)
orig_output = tf.constant(123, shape=[1,3,2,4,1], dtype=tf.float32)
grad = tf.constant(100, shape=[1,3,2,4,1], dtype=tf.float32)
tf.raw_ops.MaxPool3DGradGrad(orig_input=orig_input, orig_output=orig_output, grad=grad, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
