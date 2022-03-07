# Signal -6;2022-03-04 18:44:30.457233: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:44:30.459605: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (2 vs. 1)Asking for tensor of 2 dimensions from a tensor of 1 dimensions

# BoostedTreesSparseAggregateStatsOp

import tensorflow as tf

max_splits = 2
num_buckets = 2
node_ids = tf.constant(0, shape=[10], dtype=tf.int32)
gradients = tf.constant(2.41642356, shape=[10,2], dtype=tf.float32)
hessians = tf.constant(2.41642356, shape=[10,2], dtype=tf.float32)
feature_indices = tf.constant(0, shape=[10], dtype=tf.int32)
feature_values = tf.constant(0, shape=[10], dtype=tf.int32)
feature_shape = tf.constant(0, shape=[10], dtype=tf.int32)
tf.raw_ops.BoostedTreesSparseAggregateStats(node_ids=node_ids, gradients=gradients, hessians=hessians, feature_indices=feature_indices, feature_values=feature_values, feature_shape=feature_shape, max_splits=max_splits, num_buckets=num_buckets)