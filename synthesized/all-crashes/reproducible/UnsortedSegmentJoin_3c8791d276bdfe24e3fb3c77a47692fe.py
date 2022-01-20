# Signal -6;2022-01-20 07:06:21.219248: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:06:21.221538: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-20 07:06:21.222376: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 4)Must have a one element tensor

import tensorflow as tf

arg_0 = tf.constant("this", shape=[4], dtype=tf.string)
arg_1 = tf.constant(1, shape=[], dtype=tf.int32)
arg_2 = tf.constant(0, shape=[4], dtype=tf.int32)
tf.raw_ops.UnsortedSegmentJoin(inputs=arg_0, segment_ids=arg_1, num_segments=arg_2)