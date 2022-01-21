import tensorflow as tf

arg_0 = tf.constant(1, shape=[2], dtype=tf.int32)
arg_1 = tf.constant(0, shape=[], dtype=tf.float32)
arg_2 = tf.constant("[]", shape=[], dtype=tf.string)
arg_3 = tf.constant(65534, shape=[22], dtype=tf.int32)
arg_4 = tf.constant(0, shape=[], dtype=tf.float32)
arg_5 = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
arg_6 = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
arg_7 = tf.constant(0, shape=[4,1,3,4], dtype=tf.float32)
tf.raw_ops.BoostedTreesCalculateBestFeatureSplitV2(node_id_range=arg_0, stats_summaries_list=arg_1, split_types=arg_2, candidate_feature_ids=arg_3, l1=arg_4, l2=arg_5, tree_complexity=arg_6, min_node_weight=arg_7)