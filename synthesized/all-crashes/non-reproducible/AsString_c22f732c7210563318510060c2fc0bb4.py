# 2022-04-07 20:01:10.121899: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:10.124285: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# AsStringOp

import tensorflow as tf

precision = -1
scientific = False
shortest = False
width = -1
fill = ""
input = tf.constant(False, shape=[], dtype=tf.bool)
tf.raw_ops.AsString(input=input, precision=precision, scientific=scientific, shortest=shortest, width=width, fill=fill)
