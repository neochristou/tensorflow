# Signal -11;2022-04-07 20:02:47.838017: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:47.840201: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# QuantizedMatMulOp

import tensorflow as tf

Toutput = tf.qint32
transpose_a = True
transpose_b = False
Tactivation = tf.quint8
a = tf.constant(11, shape=[3,4], dtype=tf.quint8)
b = tf.constant(11, shape=[3,4], dtype=tf.quint8)
min_a = tf.constant([], shape=[0], dtype=tf.float32)
max_a = tf.constant(-12, shape=[1], dtype=tf.float32)
min_b = tf.constant(-12, shape=[1], dtype=tf.float32)
max_b = tf.constant(-12, shape=[1], dtype=tf.float32)
tf.raw_ops.QuantizedMatMul(a=a, b=b, min_a=min_a, max_a=max_a, min_b=min_b, max_b=max_b, Toutput=Toutput, transpose_a=transpose_a, transpose_b=transpose_b, Tactivation=Tactivation)
