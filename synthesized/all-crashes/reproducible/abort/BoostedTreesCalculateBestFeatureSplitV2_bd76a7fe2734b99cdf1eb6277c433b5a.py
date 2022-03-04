# Signal -6;2022-03-04 18:44:27.128880: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-04 18:44:27.131974: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (4 vs. 3)Asking for tensor of 4 dimensions from a tensor of 3 dimensions

# BoostedTreesCalculateBestFeatureSplitV2

import tensorflow as tf

logits_dimension = 2
node_id_range = tf.constant([1,3], shape=[2], dtype=tf.int32)
stats_summaries_list = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
split_types = tf.constant("inequality", shape=[1], dtype=tf.string)
candidate_feature_ids = tf.constant([1,3], shape=[2], dtype=tf.int32)
l1 = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
l2 = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
tree_complexity = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
min_node_weight = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
tf.raw_ops.BoostedTreesCalculateBestFeatureSplitV2(node_id_range=node_id_range, stats_summaries_list=stats_summaries_list, split_types=split_types, candidate_feature_ids=candidate_feature_ids, l1=l1, l2=l2, tree_complexity=tree_complexity, min_node_weight=min_node_weight, logits_dimension=logits_dimension)