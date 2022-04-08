# Signal -11;2022-04-07 20:02:46.782794: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:46.785686: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# QuantizedInstanceNorm

import tensorflow as tf

output_range_given = False
given_y_min = 0
given_y_max = 0
variance_epsilon = 1e-05
min_separation = 0.001
x = tf.constant(0, shape=[1,4,4,32], dtype=tf.quint8)
x_min = tf.constant([], shape=[0], dtype=tf.float32)
x_max = tf.constant(2, shape=[], dtype=tf.float32)
tf.raw_ops.QuantizedInstanceNorm(x=x, x_min=x_min, x_max=x_max, output_range_given=output_range_given, given_y_min=given_y_min, given_y_max=given_y_max, variance_epsilon=variance_epsilon, min_separation=min_separation)
