# Signal -6;2022-03-04 18:44:32.467725: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:44:32.469963: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (1 vs. 0)Asking for tensor of 1 dimensions from a tensor of 0 dimensions

# Conv3DBackpropFilterOp

import tensorflow as tf

strides = [1, 1, 1, 1, 1]
padding = "VALID"
data_format = "NDHWC"
dilations = [1, 1, 1, 1, 1]
input = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
filter_sizes = tf.constant(0, shape=[], dtype=tf.int32)
out_backprop = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
tf.raw_ops.Conv3DBackpropFilterV2(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop, strides=strides, padding=padding, data_format=data_format, dilations=dilations)