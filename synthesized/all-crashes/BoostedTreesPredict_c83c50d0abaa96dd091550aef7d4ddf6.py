import tensorflow as tf

arg_0 = tf.constant(?, shape=[], dtype=tf.resource)
arg_1 = tf.constant(0, shape=[3], dtype=tf.int32)
arg_2 = tf.constant(13, shape=[3], dtype=tf.int32)
tf.raw_ops.BoostedTreesPredict(tree_ensemble_handle=arg_0, bucketized_features=arg_1, logits_dimension=arg_2)