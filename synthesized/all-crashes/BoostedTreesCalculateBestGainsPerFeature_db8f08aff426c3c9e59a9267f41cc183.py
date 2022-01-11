import tensorflow as tf

arg_0 = tf.constant(0, shape=[2], dtype=tf.int32)
arg_1 = tf.constant(3.5e+35, shape=[17,14], dtype=tf.float32)
arg_2 = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
arg_3 = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
arg_4 = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
arg_5 = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
arg_6 = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
tf.raw_ops.BoostedTreesCalculateBestGainsPerFeature(node_id_range=arg_0, stats_summary_list=arg_1, l1=arg_2, l2=arg_3, tree_complexity=arg_4, min_node_weight=arg_5, max_splits=arg_6)