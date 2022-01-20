# Signal -6;2022-01-20 07:04:07.785986: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:04:07.788115: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-20 07:04:07.800582: F tensorflow/core/framework/tensor_shape.cc:569] Check failed: size >= 0 (-536870912 vs. 0)

import tensorflow as tf

arg_0 = tf.constant(-3.5e+35, shape=[1,61,41,1], dtype=tf.float32)
arg_1 = tf.constant(-536870912, shape=[2], dtype=tf.int32)
arg_2 = tf.constant(123, shape=[1,61,41,1], dtype=tf.float32)
tf.raw_ops.ExtractGlimpse(input=arg_0, size=arg_1, offsets=arg_2)