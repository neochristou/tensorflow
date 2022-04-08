# Signal -6;2022-04-07 20:01:43.327811: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:43.330014: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:43.330890: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 0)Must have a one element tensor

# GetSessionTensorOp

import tensorflow as tf

dtype = tf.float32
handle = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.GetSessionTensor(handle=handle, dtype=dtype)
