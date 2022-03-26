# Signal -6;2022-03-26 16:54:32.273094: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-26 16:54:32.276588: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 0)Must have a one element tensor

# GetSessionTensorOp

import tensorflow as tf

dtype = tf.float32
handle = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.GetSessionTensor(handle=handle, dtype=dtype)