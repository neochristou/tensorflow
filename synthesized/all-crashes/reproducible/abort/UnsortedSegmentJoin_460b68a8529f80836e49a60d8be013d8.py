# Signal -6;2022-02-15 18:05:02.125043: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-02-15 18:05:02.129915: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 12)Must have a one element tensor

import tensorflow as tf

inputs = tf.constant("this", shape=[12], dtype=tf.string)
segment_ids = tf.constant(0, shape=[12], dtype=tf.int64)
num_segments = tf.constant(0, shape=[12], dtype=tf.int64)
tf.raw_ops.UnsortedSegmentJoin(inputs=inputs, segment_ids=segment_ids, num_segments=num_segments)