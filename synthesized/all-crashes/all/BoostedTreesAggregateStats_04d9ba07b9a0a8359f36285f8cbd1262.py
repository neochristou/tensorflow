import tensorflow as tf

max_splits = 3
node_ids = tf.constant(1, shape=[8], dtype=tf.int32)
gradients = tf.constant(.10, shape=[8,1], dtype=tf.float32)
hessians = tf.constant(.10, shape=[8,1], dtype=tf.float32)
feature = tf.constant(1, shape=[8], dtype=tf.int32)
tf.raw_ops.BoostedTreesAggregateStats(node_ids=node_ids, gradients=gradients, hessians=hessians, feature=feature, max_splits=max_splits)