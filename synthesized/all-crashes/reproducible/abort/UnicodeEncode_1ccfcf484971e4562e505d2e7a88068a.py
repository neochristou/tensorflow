# Signal -6;2022-04-07 20:03:16.926020: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:16.927909: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:03:16.930171: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Internal: Expected shape dimensions to be non-negative, got -1

# UnicodeEncodeOp

import tensorflow as tf

output_encoding = "UTF-8"
errors = "strict"
replacement_char = 65533
input_values = tf.constant([], shape=[0], dtype=tf.int32)
input_splits = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.UnicodeEncode(input_values=input_values, input_splits=input_splits, output_encoding=output_encoding, errors=errors, replacement_char=replacement_char)
