# Signal --4;2022-04-07 20:02:07.938834: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:07.940988: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.

# MapUnstageNoKeyOp

import tensorflow as tf

dtypes = [tf.int32]
capacity = 3
memory_limit = 0
container = ""
shared_name = "MapStagingArea"
indices = tf.constant(-536870912, shape=[1], dtype=tf.int32)
tf.raw_ops.OrderedMapUnstageNoKey(indices=indices, dtypes=dtypes, capacity=capacity, memory_limit=memory_limit, container=container, shared_name=shared_name)
