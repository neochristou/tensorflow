import tensorflow as tf

arg_0 = tf.constant(0, shape=[], dtype=tf.int32)
arg_1 = tf.constant(.10, shape=[8,1], dtype=tf.float32)
arg_2 = tf.constant(.10, shape=[8,1], dtype=tf.float32)
arg_3 = tf.constant(1, shape=[8], dtype=tf.int32)
tf.raw_ops.BoostedTreesMakeStatsSummary(node_ids=arg_0, gradients=arg_1, hessians=arg_2, bucketized_features_list=arg_3)