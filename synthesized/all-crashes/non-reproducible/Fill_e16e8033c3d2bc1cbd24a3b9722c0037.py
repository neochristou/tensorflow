# 2022-02-15 18:03:56.823729: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-02-15 18:03:56.827541: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 7516192768 exceeds 10% of free system memory.

import tensorflow as tf

dims = tf.constant(1879048192, shape=[], dtype=tf.int32)
value = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.Fill(dims=dims, value=value)