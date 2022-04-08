# Signal -6;2022-04-07 20:03:02.414926: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:02.417197: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:03:02.450856: F ./tensorflow/core/framework/tensor.h:806] Check failed: NDIMS == new_sizes.size() (2 vs. 1)

# SoftmaxXentWithLogitsOp

import tensorflow as tf

features = tf.constant(0, shape=[], dtype=tf.float32)
labels = tf.constant(1, shape=[8,3], dtype=tf.float32)
tf.raw_ops.SoftmaxCrossEntropyWithLogits(features=features, labels=labels)
