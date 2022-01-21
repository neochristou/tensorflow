# Signal -6;2022-01-20 07:05:52.719738: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:05:52.721935: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-20 07:05:52.722747: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Internal: Expected shape dimensions to be non-negative, got -1879048192

import tensorflow as tf

arg_0 = tf.constant(0, shape=[3,2], dtype=tf.int64)
arg_1 = tf.constant(0, shape=[3], dtype=tf.int64)
arg_2 = tf.constant(-1879048192, shape=[3], dtype=tf.int64)
arg_3 = tf.constant(0, shape=[], dtype=tf.int64)
tf.raw_ops.SparseFillEmptyRows(indices=arg_0, values=arg_1, dense_shape=arg_2, default_value=arg_3)