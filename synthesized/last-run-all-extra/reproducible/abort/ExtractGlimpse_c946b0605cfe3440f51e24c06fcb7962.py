# Signal -6;2022-01-31 11:00:15.221168: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-31 11:00:15.223543: F tensorflow/core/framework/tensor_shape.cc:569] Check failed: size >= 0 (-536870912 vs. 0)

import tensorflow as tf

input = tf.constant(123, shape=[1,61,41,1], dtype=tf.float32)
size = tf.constant(-536870912, shape=[2], dtype=tf.int32)
offsets = tf.constant(123, shape=[1,61,41,1], dtype=tf.float32)
tf.raw_ops.ExtractGlimpse(input=input, size=size, offsets=offsets)