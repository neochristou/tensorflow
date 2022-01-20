# Signal -6;2022-01-20 07:05:47.880030: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:05:47.882170: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-20 07:05:47.883464: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 0)Must have a one element tensor

import tensorflow as tf

arg_0 = tf.constant([], shape=[0,2], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0,2], dtype=tf.int64)
arg_2 = tf.constant([], shape=[0,2], dtype=tf.int64)
arg_3 = tf.constant("[]", shape=[0], dtype=tf.string)
arg_4 = tf.constant("[]", shape=[0], dtype=tf.string)
arg_5 = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.SparseCrossV2(indices=arg_0, values=arg_1, shapes=arg_2, dense_inputs=arg_3, sep=arg_4, name=arg_5)