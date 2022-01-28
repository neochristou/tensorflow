import tensorflow as tf

node_ids = tf.constant(-65534, shape=[], dtype=tf.int32)
gradients = tf.constant(3.5e+35, shape=[21,17], dtype=tf.float32)
hessians = tf.constant(2.41642356, shape=[10,2], dtype=tf.float32)
feature_indices = tf.constant(0, shape=[10], dtype=tf.int32)
feature_values = tf.constant(0, shape=[10], dtype=tf.int32)
feature_shape = tf.constant(0, shape=[10], dtype=tf.int32)
tf.raw_ops.BoostedTreesSparseAggregateStats(node_ids=node_ids, gradients=gradients, hessians=hessians, feature_indices=feature_indices, feature_values=feature_values, feature_shape=feature_shape)