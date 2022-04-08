# 2022-04-07 20:01:44.385262: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:44.387225: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# LinSpaceOp

import tensorflow as tf

start = tf.constant(-3.5e+35, shape=[], dtype=tf.float32)
stop = tf.constant(3, shape=[], dtype=tf.float32)
num = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.LinSpace(start=start, stop=stop, num=num)
