# MaxPoolingGradOp

import tensorflow as tf

ksize = [1, 1, 1, 1]
strides = [1, 1, 1, 1]
padding = "VALID"
data_format = "NHWC"
orig_input = tf.constant(-1, shape=[2,1,5,2], dtype=tf.float32)
orig_output = tf.constant(-1, shape=[2,1,5,2], dtype=tf.float32)
grad = tf.constant(1, shape=[2,1,5,2], dtype=tf.float32)
tf.raw_ops.MaxPoolGradV2(orig_input=orig_input, orig_output=orig_output, grad=grad, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
