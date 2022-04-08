# Signal -6;2022-04-07 20:01:36.484473: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:36.486839: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:36.487999: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (1 vs. 4)Asking for tensor of 1 dimensions from a tensor of 4 dimensions

# FakeQuantWithMinMaxVarsPerChannelOp

import tensorflow as tf

num_bits = 8
narrow_range = False
inputs = tf.constant(-3.5e+35, shape=[10,19,22], dtype=tf.float32)
min = tf.constant(3.5e+35, shape=[22,19,5,13], dtype=tf.float32)
max = tf.constant(3.5e+35, shape=[22,19,5,13], dtype=tf.float32)
tf.raw_ops.FakeQuantWithMinMaxVarsPerChannel(inputs=inputs, min=min, max=max, num_bits=num_bits, narrow_range=narrow_range)
