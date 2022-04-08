# Signal -11;2022-04-07 20:02:50.967476: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:50.969637: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# QuantizedRelu6Op

import tensorflow as tf

out_type = tf.quint8
features = tf.constant(28, shape=[4,2], dtype=tf.quint8)
min_features = tf.constant([], shape=[0], dtype=tf.float32)
max_features = tf.constant(-128, shape=[1], dtype=tf.float32)
tf.raw_ops.QuantizedRelu6(features=features, min_features=min_features, max_features=max_features, out_type=out_type)
