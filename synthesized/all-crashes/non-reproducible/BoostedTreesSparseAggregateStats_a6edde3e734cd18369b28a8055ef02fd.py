# 2022-01-20 07:03:51.200217: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:03:51.202247: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/BoostedTreesSparseAggregateStats_a6edde3e734cd18369b28a8055ef02fd.py", line 9, in <module>    tf.raw_ops.BoostedTreesSparseAggregateStats(node_ids=arg_0, gradients=arg_1, hessians=arg_2, feature_indices=arg_3, feature_values=arg_4, feature_shape=arg_5)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: boosted_trees_sparse_aggregate_stats() missing 2 required positional arguments: 'max_splits' and 'num_buckets'

import tensorflow as tf

arg_0 = tf.constant(536870912, shape=[], dtype=tf.int32)
arg_1 = tf.constant(2.41642356, shape=[10,2], dtype=tf.float32)
arg_2 = tf.constant(2.41642356, shape=[10,2], dtype=tf.float32)
arg_3 = tf.constant(0, shape=[10], dtype=tf.int32)
arg_4 = tf.constant(0, shape=[10], dtype=tf.int32)
arg_5 = tf.constant(0, shape=[10], dtype=tf.int32)
tf.raw_ops.BoostedTreesSparseAggregateStats(node_ids=arg_0, gradients=arg_1, hessians=arg_2, feature_indices=arg_3, feature_values=arg_4, feature_shape=arg_5)