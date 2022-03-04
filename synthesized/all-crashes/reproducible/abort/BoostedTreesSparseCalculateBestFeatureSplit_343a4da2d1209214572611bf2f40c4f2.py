# Signal -6;2022-03-04 18:44:31.464378: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:44:31.466637: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (2 vs. 1)Asking for tensor of 2 dimensions from a tensor of 1 dimensions

# BoostedTreesSparseCalculateBestFeatureSplitOp

import tensorflow as tf

logits_dimension = 1
split_type = "inequality"
node_id_range = tf.constant([1,3], shape=[2], dtype=tf.int32)
stats_summary_indices = tf.constant([1,3], shape=[2], dtype=tf.int32)
stats_summary_values = tf.constant(0.15, shape=[24], dtype=tf.float32)
stats_summary_shape = tf.constant([1,3], shape=[2], dtype=tf.int32)
l1 = tf.constant(0.15, shape=[24], dtype=tf.float32)
l2 = tf.constant(0.15, shape=[24], dtype=tf.float32)
tree_complexity = tf.constant(0.15, shape=[24], dtype=tf.float32)
min_node_weight = tf.constant(0.15, shape=[24], dtype=tf.float32)
tf.raw_ops.BoostedTreesSparseCalculateBestFeatureSplit(node_id_range=node_id_range, stats_summary_indices=stats_summary_indices, stats_summary_values=stats_summary_values, stats_summary_shape=stats_summary_shape, l1=l1, l2=l2, tree_complexity=tree_complexity, min_node_weight=min_node_weight, logits_dimension=logits_dimension, split_type=split_type)