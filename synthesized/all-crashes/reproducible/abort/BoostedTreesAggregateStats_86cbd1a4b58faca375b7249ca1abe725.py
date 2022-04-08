# Signal -6;2022-04-07 20:01:17.573052: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:17.575023: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:17.590141: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (2 vs. 1)Asking for tensor of 2 dimensions from a tensor of 1 dimensions

# BoostedTreesAggregateStatsOp

import tensorflow as tf

max_splits = 3
num_buckets = 4
node_ids = tf.constant(1, shape=[8], dtype=tf.int32)
gradients = tf.constant(.10, shape=[8,1], dtype=tf.float32)
hessians = tf.constant(.10, shape=[8,1], dtype=tf.float32)
feature = tf.constant(1, shape=[8], dtype=tf.int32)
tf.raw_ops.BoostedTreesAggregateStats(node_ids=node_ids, gradients=gradients, hessians=hessians, feature=feature, max_splits=max_splits, num_buckets=num_buckets)
