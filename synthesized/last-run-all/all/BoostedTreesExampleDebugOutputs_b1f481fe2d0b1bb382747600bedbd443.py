import tensorflow as tf

tree_ensemble_handle = tf.constant(36, shape=[2], dtype=tf.int32)
bucketized_features = tf.constant(1879048192, shape=[], dtype=tf.int32)
logits_dimension = tf.constant(36, shape=[2], dtype=tf.int32)
tf.raw_ops.BoostedTreesExampleDebugOutputs(tree_ensemble_handle=tree_ensemble_handle, bucketized_features=bucketized_features, logits_dimension=logits_dimension)