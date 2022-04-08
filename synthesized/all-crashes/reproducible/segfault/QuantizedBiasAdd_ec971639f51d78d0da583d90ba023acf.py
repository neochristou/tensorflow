# Signal -11;2022-04-07 20:02:44.648072: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:44.650298: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# QuantizedBiasAddOp

import tensorflow as tf

out_type = tf.qint32
input = tf.constant(43, shape=[2,3], dtype=tf.quint8)
bias = tf.constant(43, shape=[2,3], dtype=tf.quint8)
min_input = tf.constant([], shape=[0], dtype=tf.float32)
max_input = tf.constant(0, shape=[1], dtype=tf.float32)
min_bias = tf.constant(0, shape=[1], dtype=tf.float32)
max_bias = tf.constant(0, shape=[1], dtype=tf.float32)
tf.raw_ops.QuantizedBiasAdd(input=input, bias=bias, min_input=min_input, max_input=max_input, min_bias=min_bias, max_bias=max_bias, out_type=out_type)
