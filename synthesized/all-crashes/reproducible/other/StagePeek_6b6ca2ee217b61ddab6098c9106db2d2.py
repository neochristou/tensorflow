# Signal --4;2022-03-04 18:47:45.640338: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# StagePeekOp

import tensorflow as tf

dtypes = [tf.int32]
capacity = 0
memory_limit = 0
container = ""
shared_name = "StagingArea"
index = tf.constant(-536870912, shape=[], dtype=tf.int32)
tf.raw_ops.StagePeek(index=index, dtypes=dtypes, capacity=capacity, memory_limit=memory_limit, container=container, shared_name=shared_name)