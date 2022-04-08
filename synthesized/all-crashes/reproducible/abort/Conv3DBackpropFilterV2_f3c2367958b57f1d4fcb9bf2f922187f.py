# Signal -6;2022-04-07 20:01:25.434630: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:25.436828: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:25.439016: F tensorflow/core/kernels/mkl/mkl_conv_grad_filter_ops.cc:643] Check failed: TensorShapeUtils::IsVector(filter_tensor.shape()) == true (0 vs. 1)

# Conv3DCustomBackpropFilterOp

import tensorflow as tf

strides = [1, 2, 2, 2, 1]
padding = "SAME"
data_format = "NDHWC"
dilations = [1, 1, 1, 1, 1]
input = tf.constant(1, shape=[2,6,8,6,2], dtype=tf.float32)
filter_sizes = tf.constant(0, shape=[], dtype=tf.int32)
out_backprop = tf.constant(1, shape=[2,6,8,6,2], dtype=tf.float32)
tf.raw_ops.Conv3DBackpropFilterV2(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop, strides=strides, padding=padding, data_format=data_format, dilations=dilations)
