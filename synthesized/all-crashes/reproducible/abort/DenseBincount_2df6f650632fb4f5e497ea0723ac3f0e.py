# Signal -6;2022-04-07 20:01:27.559928: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:27.562084: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:27.576013: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 8)Must have a one element tensor

# DenseBincountOp

import tensorflow as tf

binary_output = False
input = tf.constant(1, shape=[2,4], dtype=tf.int64)
size = tf.constant(1, shape=[2,4], dtype=tf.int64)
weights = tf.constant([], shape=[0], dtype=tf.float32)
tf.raw_ops.DenseBincount(input=input, size=size, weights=weights, binary_output=binary_output)
