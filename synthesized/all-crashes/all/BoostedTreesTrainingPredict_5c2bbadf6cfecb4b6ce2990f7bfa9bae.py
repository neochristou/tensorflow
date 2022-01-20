import tensorflow as tf

arg_0 = tf.constant(?, shape=[], dtype=tf.resource)
arg_1 = tf.constant(36, shape=[2], dtype=tf.int32)
arg_2 = tf.constant(0, shape=[2], dtype=tf.int32)
arg_3 = tf.constant(0, shape=[2], dtype=tf.int32)
arg_4 = tf.constant(0, shape=[2], dtype=tf.int32)
tf.raw_ops.BoostedTreesTrainingPredict(tree_ensemble_handle=arg_0, cached_tree_ids=arg_1, cached_node_ids=arg_2, bucketized_features=arg_3, logits_dimension=arg_4)