# Signal -11;2022-04-07 20:02:41.435133: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:41.437462: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# QuantizedAddOp

import tensorflow as tf

Toutput = tf.qint32
x = tf.constant(26, shape=[10], dtype=tf.quint8)
y = tf.constant(26, shape=[10], dtype=tf.quint8)
min_x = tf.constant([], shape=[0], dtype=tf.float32)
max_x = tf.constant(0, shape=[], dtype=tf.float32)
min_y = tf.constant(0, shape=[], dtype=tf.float32)
max_y = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.QuantizedAdd(x=x, y=y, min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y, Toutput=Toutput)
