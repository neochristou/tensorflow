# Signal -6;2022-04-07 20:01:28.652452: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:28.654703: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:28.671161: F tensorflow/core/kernels/mkl/mkl_conv_grad_filter_ops.cc:647] Check failed: TensorShapeUtils::MakeShape(filter_tensor.vec<int32>(), &filter_tf_shape) .ok() == true (0 vs. 1)

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
