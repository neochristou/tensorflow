# 2022-01-28 15:26:28.668707: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/BoostedTreesSparseAggregateStats_81559f3c81c4e381cd6101e91e430a18.py", line 9, in <module>    tf.raw_ops.BoostedTreesSparseAggregateStats(node_ids=node_ids, gradients=gradients, hessians=hessians, feature_indices=feature_indices, feature_values=feature_values, feature_shape=feature_shape)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: boosted_trees_sparse_aggregate_stats() missing 2 required positional arguments: 'max_splits' and 'num_buckets'

import tensorflow as tf

node_ids = tf.constant(-65534, shape=[], dtype=tf.int32)
gradients = tf.constant(3.5e+35, shape=[21,17], dtype=tf.float32)
hessians = tf.constant(2.41642356, shape=[10,2], dtype=tf.float32)
feature_indices = tf.constant(0, shape=[10], dtype=tf.int32)
feature_values = tf.constant(0, shape=[10], dtype=tf.int32)
feature_shape = tf.constant(0, shape=[10], dtype=tf.int32)
tf.raw_ops.BoostedTreesSparseAggregateStats(node_ids=node_ids, gradients=gradients, hessians=hessians, feature_indices=feature_indices, feature_values=feature_values, feature_shape=feature_shape)