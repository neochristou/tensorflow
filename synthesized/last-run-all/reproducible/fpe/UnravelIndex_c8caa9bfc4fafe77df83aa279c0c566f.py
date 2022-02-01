# Signal -8;2022-01-31 21:31:19.084814: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

import tensorflow as tf

indices = tf.constant(-536870912, shape=[3], dtype=tf.int32)
dims = tf.constant(-536870912, shape=[3], dtype=tf.int32)
tf.raw_ops.UnravelIndex(indices=indices, dims=dims)