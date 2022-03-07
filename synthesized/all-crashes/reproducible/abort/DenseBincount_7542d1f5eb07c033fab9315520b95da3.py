# Signal -6;2022-03-04 18:44:35.505983: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:44:35.508091: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 6)Must have a one element tensor

# DenseBincountOp

import tensorflow as tf

binary_output = False
input = tf.constant(1, shape=[2,3], dtype=tf.int32)
size = tf.constant(1, shape=[2,3], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.float32)
tf.raw_ops.DenseBincount(input=input, size=size, weights=weights, binary_output=binary_output)