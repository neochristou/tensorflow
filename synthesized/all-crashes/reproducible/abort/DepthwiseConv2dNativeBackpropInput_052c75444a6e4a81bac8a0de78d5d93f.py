# Signal -6;2022-03-07 19:06:21.921268: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory2022-03-07 19:06:21.921319: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.2022-03-07 19:06:22.829175: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory2022-03-07 19:06:22.829224: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)2022-03-07 19:06:22.829295: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (devel): /proc/driver/nvidia/version does not exist2022-03-07 19:06:22.829572: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-07 19:06:22.833534: F tensorflow/core/framework/tensor_shape.cc:404] Check failed: 0 <= new_num_elements (0 vs. -1)

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