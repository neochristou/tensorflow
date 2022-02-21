import tensorflow as tf

node_id_range = tf.constant(1, shape=[2], dtype=tf.int32)
stats_summaries_list = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
split_types = tf.constant("inequality", shape=[1], dtype=tf.string)
candidate_feature_ids = tf.constant(1, shape=[2], dtype=tf.int32)
l1 = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
l2 = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
tree_complexity = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
min_node_weight = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
tf.raw_ops.BoostedTreesCalculateBestFeatureSplitV2(node_id_range=node_id_range, stats_summaries_list=stats_summaries_list, split_types=split_types, candidate_feature_ids=candidate_feature_ids, l1=l1, l2=l2, tree_complexity=tree_complexity, min_node_weight=min_node_weight)