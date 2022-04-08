# Signal -6;2022-04-07 20:01:29.730480: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:29.732743: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:29.784720: F tensorflow/core/kernels/mkl/mkl_conv_grad_input_ops.cc:531] Non-OK-status: tensor::MakeShape(input_tensor, &input_tf_shape) status: Invalid argument: Shape [1879048192,1879048192,1879048192,1879048192,1879048192,1879048192,1879048192,1879048192,1879048192,1879048192,1879048192,1879048192,1879048192] would have more than 2**63 - 1 elements

# DepthwiseConv2dNativeBackpropInputOp

import tensorflow as tf

strides = [1, 1, 1, 1]
padding = "SAME"
explicit_paddings = []
data_format = "NHWC"
dilations = [1, 1, 1, 1]
input_sizes = tf.constant(1879048192, shape=[13], dtype=tf.int32)
filter = tf.constant(0.184634328, shape=[1,1,48,2], dtype=tf.float32)
out_backprop = tf.constant(0.184634328, shape=[1,1,48,2], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropInput(input_sizes=input_sizes, filter=filter, out_backprop=out_backprop, strides=strides, padding=padding, explicit_paddings=explicit_paddings, data_format=data_format, dilations=dilations)
