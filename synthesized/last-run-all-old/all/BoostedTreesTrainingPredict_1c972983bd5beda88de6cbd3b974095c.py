import tensorflow as tf

tree_ensemble_handle = tf.constant(0, shape=[2], dtype=tf.int32)
cached_tree_ids = tf.constant(36, shape=[2], dtype=tf.int32)
cached_node_ids = tf.constant(0, shape=[2], dtype=tf.int32)
bucketized_features = tf.constant(0, shape=[2], dtype=tf.int32)
tf.raw_ops.BoostedTreesTrainingPredict(tree_ensemble_handle=tree_ensemble_handle, cached_tree_ids=cached_tree_ids, cached_node_ids=cached_node_ids, bucketized_features=bucketized_features)