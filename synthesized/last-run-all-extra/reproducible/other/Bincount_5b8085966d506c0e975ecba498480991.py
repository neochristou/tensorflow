# Signal --4;2022-01-31 10:59:27.686189: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-31 10:59:27.688283: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 73014444032 exceeds 10% of free system memory.

import tensorflow as tf

arr = tf.constant(0, shape=[5], dtype=tf.int32)
size = tf.constant(536870912, shape=[], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.int64)
tf.raw_ops.Bincount(arr=arr, size=size, weights=weights)