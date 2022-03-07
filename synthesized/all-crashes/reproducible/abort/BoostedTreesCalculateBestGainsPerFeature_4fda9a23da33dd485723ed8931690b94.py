# Signal -6;2022-03-04 18:44:28.145083: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:44:28.148866: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (3 vs. 2)Asking for tensor of 3 dimensions from a tensor of 2 dimensions

# BoostedTreesCalculateBestGainsPerFeatureOp

import tensorflow as tf

max_splits = 7
node_id_range = tf.constant([1,3], shape=[2], dtype=tf.int32)
stats_summary_list = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
l1 = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
l2 = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
tree_complexity = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
min_node_weight = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
tf.raw_ops.BoostedTreesCalculateBestGainsPerFeature(node_id_range=node_id_range, stats_summary_list=stats_summary_list, l1=l1, l2=l2, tree_complexity=tree_complexity, min_node_weight=min_node_weight, max_splits=max_splits)