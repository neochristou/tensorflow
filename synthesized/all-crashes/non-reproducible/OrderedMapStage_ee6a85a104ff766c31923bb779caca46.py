# 2022-03-07 18:54:20.070787: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# MapStageOp

import tensorflow as tf

dtypes = [tf.int32]
capacity = 3
memory_limit = 0
container = ""
shared_name = "MapStagingArea"
key = tf.constant(-1250999896764, shape=[], dtype=tf.int64)
indices = tf.constant(0, shape=[1], dtype=tf.int32)
values = tf.constant(0, shape=[1], dtype=tf.int32)
tf.raw_ops.OrderedMapStage(key=key, indices=indices, values=values, dtypes=dtypes, capacity=capacity, memory_limit=memory_limit, container=container, shared_name=shared_name)