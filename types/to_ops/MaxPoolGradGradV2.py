# MaxPoolingGradGradOp

import tensorflow as tf

padding = "VALID"
data_format = "NHWC"
orig_input = tf.constant(123, shape=[1,3,3,1], dtype=tf.float32)
orig_output = tf.constant(123, shape=[1,3,3,1], dtype=tf.float32)
grad = tf.constant(01, shape=[1,3,3,1], dtype=tf.float32)
ksize = tf.constant(1, shape=[4], dtype=tf.int32)
strides = tf.constant(1, shape=[4], dtype=tf.int32)
tf.raw_ops.MaxPoolGradGradV2(orig_input=orig_input, orig_output=orig_output, grad=grad, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
