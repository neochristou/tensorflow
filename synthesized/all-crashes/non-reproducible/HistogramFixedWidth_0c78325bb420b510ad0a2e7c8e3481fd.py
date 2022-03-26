# 2022-03-26 16:54:33.303124: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-26 16:54:33.306638: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 7516192768 exceeds 10% of free system memory.

# HistogramFixedWidthOp

import tensorflow as tf

dtype = tf.int32
values = tf.constant(-1.5e+300, shape=[6], dtype=tf.float64)
value_range = tf.constant([0,5], shape=[2], dtype=tf.float64)
nbins = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.HistogramFixedWidth(values=values, value_range=value_range, nbins=nbins, dtype=dtype)