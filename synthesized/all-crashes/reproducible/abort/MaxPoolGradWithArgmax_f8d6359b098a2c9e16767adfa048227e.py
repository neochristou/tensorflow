# Signal -6;2022-03-04 18:46:22.779778: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:46:22.781786: F tensorflow/core/kernels/maxpooling_op.cc:1032] Check failed: grad_out_index >= output_start && grad_out_index < output_end Invalid output gradient index: 13, 0, 8

# MaxPoolingGradWithArgmaxOp

import tensorflow as tf

ksize = [1, 2, 2, 1]
strides = [1, 1, 1, 1]
padding = "VALID"
include_batch_in_index = False
input = tf.constant(111213, shape=[2,2,2,1], dtype=tf.float32)
grad = tf.constant(111, shape=[2,3,3,1], dtype=tf.float32)
argmax = tf.constant(13, shape=[2,2,2,1], dtype=tf.int64)
tf.raw_ops.MaxPoolGradWithArgmax(input=input, grad=grad, argmax=argmax, ksize=ksize, strides=strides, padding=padding, include_batch_in_index=include_batch_in_index)