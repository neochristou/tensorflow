# Signal -11;2022-04-07 20:01:39.976017: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:39.978938: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# FusedBatchNormGradOp

import tensorflow as tf

epsilon = 0.001
data_format = "NHWC"
is_training = True
y_backprop = tf.constant(1, shape=[1,1,6,2], dtype=tf.float32)
x = tf.constant(2, shape=[1,1,6,2], dtype=tf.float32)
scale = tf.constant([], shape=[0], dtype=tf.float32)
reserve_space_1 = tf.constant([4,4], shape=[2], dtype=tf.float32)
reserve_space_2 = tf.constant([4,4], shape=[2], dtype=tf.float32)
tf.raw_ops.FusedBatchNormGradV2(y_backprop=y_backprop, x=x, scale=scale, reserve_space_1=reserve_space_1, reserve_space_2=reserve_space_2, epsilon=epsilon, data_format=data_format, is_training=is_training)
