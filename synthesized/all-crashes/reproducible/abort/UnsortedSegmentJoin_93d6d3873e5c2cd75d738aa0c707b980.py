# Signal -6;2022-04-07 20:03:19.095621: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:19.097461: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:03:19.098805: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 12)Must have a one element tensor

# UnsortedSegmentJoinOp

import tensorflow as tf

separator = ""
inputs = tf.constant("this", shape=[12], dtype=tf.string)
segment_ids = tf.constant(0, shape=[12], dtype=tf.int64)
num_segments = tf.constant(0, shape=[12], dtype=tf.int64)
tf.raw_ops.UnsortedSegmentJoin(inputs=inputs, segment_ids=segment_ids, num_segments=num_segments, separator=separator)
