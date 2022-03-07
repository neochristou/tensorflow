# Signal -6;2022-03-04 18:46:55.119787: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:46:55.121769: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 0)Must have a one element tensor

# QuantizeAndDequantizeV4GradientOp

import tensorflow as tf

axis = -1
gradients = tf.constant(1, shape=[2,2], dtype=tf.float64)
input = tf.constant(1, shape=[2,2], dtype=tf.float64)
input_min = tf.constant([], shape=[0], dtype=tf.float64)
input_max = tf.constant(-10, shape=[], dtype=tf.float64)
tf.raw_ops.QuantizeAndDequantizeV4Grad(gradients=gradients, input=input, input_min=input_min, input_max=input_max, axis=axis)