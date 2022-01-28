# Signal -6;2022-01-28 15:27:48.490989: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-28 15:27:48.502025: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 4)Must have a one element tensor

import tensorflow as tf

inputs = tf.constant("[]", shape=[0], dtype=tf.string)
segment_ids = tf.constant(0, shape=[4], dtype=tf.int32)
num_segments = tf.constant(0, shape=[4], dtype=tf.int32)
tf.raw_ops.UnsortedSegmentJoin(inputs=inputs, segment_ids=segment_ids, num_segments=num_segments)