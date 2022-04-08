# Signal -8;2022-04-07 20:03:17.997181: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:17.999556: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# UnravelIndexOp

import tensorflow as tf

indices = tf.constant(-536870912, shape=[3], dtype=tf.int32)
dims = tf.constant(-536870912, shape=[3], dtype=tf.int32)
tf.raw_ops.UnravelIndex(indices=indices, dims=dims)
