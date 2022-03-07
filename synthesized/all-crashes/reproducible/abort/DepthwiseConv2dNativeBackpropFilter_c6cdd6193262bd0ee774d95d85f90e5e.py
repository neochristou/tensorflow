# Signal -6;2022-03-04 18:44:36.538209: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:44:36.540543: F tensorflow/core/framework/tensor_shape.cc:405] Check failed: 0 <= new_num_elements (0 vs. -1)

# DepthwiseConv2dNativeBackpropFilterOp

import tensorflow as tf

strides = [1, 1, 1, 1]
padding = "SAME"
explicit_paddings = []
data_format = "NHWC"
dilations = [1, 1, 1, 1]
input = tf.constant(1, shape=[1,4,4,3], dtype=tf.float32)
filter_sizes = tf.constant(1879048192, shape=[13], dtype=tf.int32)
out_backprop = tf.constant(1, shape=[1,4,4,3], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropFilter(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop, strides=strides, padding=padding, explicit_paddings=explicit_paddings, data_format=data_format, dilations=dilations)