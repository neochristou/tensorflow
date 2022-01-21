import tensorflow as tf

arg_0 = tf.constant(36, shape=[2], dtype=tf.int32)
arg_1 = tf.constant(0, shape=[], dtype=tf.int32)
arg_2 = tf.constant(36, shape=[2], dtype=tf.int32)
tf.raw_ops.BoostedTreesExampleDebugOutputs(tree_ensemble_handle=arg_0, bucketized_features=arg_1, logits_dimension=arg_2)