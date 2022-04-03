# Signal -11;2022-03-07 18:53:05.832554: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# EditDistanceOp

import tensorflow as tf

normalize = True
hypothesis_indices = tf.constant(-1250999896764, shape=[3,3], dtype=tf.int64)
hypothesis_values = tf.constant(0, shape=[3], dtype=tf.int64)
hypothesis_shape = tf.constant(0, shape=[3], dtype=tf.int64)
truth_indices = tf.constant(-1250999896764, shape=[3,3], dtype=tf.int64)
truth_values = tf.constant(2, shape=[3], dtype=tf.int64)
truth_shape = tf.constant(2, shape=[3], dtype=tf.int64)
tf.raw_ops.EditDistance(hypothesis_indices=hypothesis_indices, hypothesis_values=hypothesis_values, hypothesis_shape=hypothesis_shape, truth_indices=truth_indices, truth_values=truth_values, truth_shape=truth_shape, normalize=normalize)