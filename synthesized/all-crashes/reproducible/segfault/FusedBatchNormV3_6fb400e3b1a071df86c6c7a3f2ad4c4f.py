# Signal -11;2022-04-07 20:01:42.135709: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:42.137945: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# FusedBatchNormOpV3

import tensorflow as tf

epsilon = 0.001
exponential_avg_factor = 1
data_format = "NHWC"
is_training = False
x = tf.constant(0, shape=[3,2,4,2], dtype=tf.float32)
scale = tf.constant([0,0], shape=[2], dtype=tf.float32)
offset = tf.constant([1,1], shape=[2], dtype=tf.float32)
mean = tf.constant([], shape=[0], dtype=tf.float32)
variance = tf.constant([1,1], shape=[2], dtype=tf.float32)
tf.raw_ops.FusedBatchNormV3(x=x, scale=scale, offset=offset, mean=mean, variance=variance, epsilon=epsilon, exponential_avg_factor=exponential_avg_factor, data_format=data_format, is_training=is_training)
