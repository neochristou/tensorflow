# Signal -6;2022-04-07 20:01:35.391148: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:35.393520: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:35.394612: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 6)Must have a one element tensor

# FakeQuantWithMinMaxVarsGradientOp

import tensorflow as tf

num_bits = 8
narrow_range = False
gradients = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
inputs = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
min = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
max = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
tf.raw_ops.FakeQuantWithMinMaxVarsGradient(gradients=gradients, inputs=inputs, min=min, max=max, num_bits=num_bits, narrow_range=narrow_range)
