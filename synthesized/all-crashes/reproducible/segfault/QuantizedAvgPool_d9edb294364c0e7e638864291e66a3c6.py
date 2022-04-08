# Signal -11;2022-04-07 20:02:43.549139: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:43.551411: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# QuantizedAvgPoolingOp

import tensorflow as tf

ksize = [1, 2, 2, 1]
strides = [1, 2, 2, 1]
padding = "SAME"
input = tf.constant(1, shape=[1,4,4,2], dtype=tf.quint8)
min_input = tf.constant([], shape=[0], dtype=tf.float32)
max_input = tf.constant(0, shape=[1], dtype=tf.float32)
tf.raw_ops.QuantizedAvgPool(input=input, min_input=min_input, max_input=max_input, ksize=ksize, strides=strides, padding=padding)
