#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/BoostedTreesTrainingPredict_cdaf69688fda8609b3bc9d04a24d2211.py", line 3    arg_0 = tf.constant(?, shape=[], dtype=tf.resource)                        ^SyntaxError: invalid syntax

import tensorflow as tf

arg_0 = tf.constant(?, shape=[], dtype=tf.resource)
arg_1 = tf.constant(-536870912, shape=[2], dtype=tf.int32)
arg_2 = tf.constant(0, shape=[2], dtype=tf.int32)
arg_3 = tf.constant(0, shape=[2], dtype=tf.int32)
arg_4 = tf.constant(0, shape=[2], dtype=tf.int32)
tf.raw_ops.BoostedTreesTrainingPredict(tree_ensemble_handle=arg_0, cached_tree_ids=arg_1, cached_node_ids=arg_2, bucketized_features=arg_3, logits_dimension=arg_4)