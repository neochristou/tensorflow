# Signal -6;2022-04-07 20:01:33.271347: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:33.273653: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:33.294944: F tensorflow/core/framework/tensor_shape.cc:569] Check failed: size >= 0 (-536870912 vs. 0)

# ExtractGlimpseOp

import tensorflow as tf

centered = True
normalized = True
uniform_noise = True
noise = "uniform"
input = tf.constant(123, shape=[1,61,41,1], dtype=tf.float32)
size = tf.constant([-536870912,-536870912], shape=[2], dtype=tf.int32)
offsets = tf.constant(123, shape=[1,61,41,1], dtype=tf.float32)
tf.raw_ops.ExtractGlimpseV2(input=input, size=size, offsets=offsets, centered=centered, normalized=normalized, uniform_noise=uniform_noise, noise=noise)
