# 2022-02-15 18:03:40.348357: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/BoostedTreesAggregateStats_8c5e1c054692732ef0d00ef80c91fe5e.py", line 7, in <module>    tf.raw_ops.BoostedTreesAggregateStats(node_ids=node_ids, gradients=gradients, hessians=hessians, feature=feature)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: boosted_trees_aggregate_stats() missing 2 required positional arguments: 'max_splits' and 'num_buckets'

import tensorflow as tf

node_ids = tf.constant(1, shape=[8], dtype=tf.int32)
gradients = tf.constant(.10, shape=[8, 1], dtype=tf.float32)
hessians = tf.constant(.10, shape=[8, 1], dtype=tf.float32)
feature = tf.constant(1, shape=[8], dtype=tf.int32)
tf.raw_ops.BoostedTreesAggregateStats(
    node_ids=node_ids, gradients=gradients, hessians=hessians, feature=feature, max_splits=3, num_buckets=4)
