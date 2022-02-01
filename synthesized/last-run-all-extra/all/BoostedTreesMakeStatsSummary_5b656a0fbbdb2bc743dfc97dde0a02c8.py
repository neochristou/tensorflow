import tensorflow as tf

node_ids = tf.constant(-536870912, shape=[8], dtype=tf.int32)
gradients = tf.constant(.10, shape=[8,1], dtype=tf.float32)
hessians = tf.constant(.10, shape=[8,1], dtype=tf.float32)
bucketized_features_list = tf.constant(1, shape=[8], dtype=tf.int32)
tf.raw_ops.BoostedTreesMakeStatsSummary(node_ids=node_ids, gradients=gradients, hessians=hessians, bucketized_features_list=bucketized_features_list)