# 2022-01-20 07:03:48.943403: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:03:48.945410: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/BoostedTreesMakeStatsSummary_eb882d7a7634d2091cf4d635a3d5675e.py", line 7, in <module>    tf.raw_ops.BoostedTreesMakeStatsSummary(node_ids=arg_0, gradients=arg_1, hessians=arg_2, bucketized_features_list=arg_3)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: boosted_trees_make_stats_summary() missing 2 required positional arguments: 'max_splits' and 'num_buckets'

import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[8], dtype=tf.int32)
arg_1 = tf.constant(.10, shape=[8,1], dtype=tf.float32)
arg_2 = tf.constant(.10, shape=[8,1], dtype=tf.float32)
arg_3 = tf.constant(1, shape=[8], dtype=tf.int32)
tf.raw_ops.BoostedTreesMakeStatsSummary(node_ids=arg_0, gradients=arg_1, hessians=arg_2, bucketized_features_list=arg_3)