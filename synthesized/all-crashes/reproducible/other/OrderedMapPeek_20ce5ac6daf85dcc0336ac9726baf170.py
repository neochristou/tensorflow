# Signal --4;2022-03-07 18:53:50.017691: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# MapPeekOp

import tensorflow as tf

dtypes = [tf.float32, tf.float32]
capacity = 0
memory_limit = 0
container = ""
shared_name = "MapStagingArea"
key = tf.constant(-1879048192, shape=[], dtype=tf.int64)
indices = tf.constant([0,2], shape=[2], dtype=tf.int32)
tf.raw_ops.OrderedMapPeek(key=key, indices=indices, dtypes=dtypes, capacity=capacity, memory_limit=memory_limit, container=container, shared_name=shared_name)