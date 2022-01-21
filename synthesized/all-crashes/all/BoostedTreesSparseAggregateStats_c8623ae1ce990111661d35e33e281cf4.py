import tensorflow as tf

arg_0 = tf.constant(0, shape=[10], dtype=tf.int32)
arg_1 = tf.constant(2.41642356, shape=[10,2], dtype=tf.float32)
arg_2 = tf.constant(2.41642356, shape=[10,2], dtype=tf.float32)
arg_3 = tf.constant(0, shape=[10], dtype=tf.int32)
arg_4 = tf.constant(0, shape=[10], dtype=tf.int32)
arg_5 = tf.constant(0, shape=[10], dtype=tf.int32)
tf.raw_ops.BoostedTreesSparseAggregateStats(node_ids=arg_0, gradients=arg_1, hessians=arg_2, feature_indices=arg_3, feature_values=arg_4, feature_shape=arg_5)