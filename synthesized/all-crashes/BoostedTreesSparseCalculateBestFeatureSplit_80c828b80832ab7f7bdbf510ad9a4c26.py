import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[2,16,22,16], dtype=tf.int32)
arg_1 = tf.constant(0, shape=[], dtype=tf.int32)
arg_2 = tf.constant(3.5e+35, shape=[2,16,22,16], dtype=tf.float32)
arg_3 = tf.constant(-1879048192, shape=[4], dtype=tf.int32)
arg_4 = tf.constant(0.15, shape=[24], dtype=tf.float32)
arg_5 = tf.constant(0.15, shape=[24], dtype=tf.float32)
arg_6 = tf.constant(0.15, shape=[24], dtype=tf.float32)
arg_7 = tf.constant(0.15, shape=[24], dtype=tf.float32)
tf.raw_ops.BoostedTreesSparseCalculateBestFeatureSplit(node_id_range=arg_0, stats_summary_indices=arg_1, stats_summary_values=arg_2, stats_summary_shape=arg_3, l1=arg_4, l2=arg_5, tree_complexity=arg_6, min_node_weight=arg_7)