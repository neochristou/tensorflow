# 2022-02-15 18:03:42.829130: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/BoostedTreesCalculateBestGainsPerFeature_4d75583bcb26cd87395c2c620dcde0ad.py", line 10, in <module>    tf.raw_ops.BoostedTreesCalculateBestGainsPerFeature(node_id_range=node_id_range, stats_summary_list=stats_summary_list, l1=l1, l2=l2, tree_complexity=tree_complexity, min_node_weight=min_node_weight, max_splits=max_splits)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_boosted_trees_ops.py", line 500, in boosted_trees_calculate_best_gains_per_feature    return boosted_trees_calculate_best_gains_per_feature_eager_fallback(  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_boosted_trees_ops.py", line 540, in boosted_trees_calculate_best_gains_per_feature_eager_fallback    raise TypeError(TypeError: Expected list for 'stats_summary_list' argument to 'boosted_trees_calculate_best_gains_per_feature' Op, not <tf.Tensor: shape=(7, 4, 2), dtype=float32, numpy=array([[[0., 0.],        [0., 0.],        [0., 0.],        [0., 0.]],       [[0., 0.],        [0., 0.],        [0., 0.],        [0., 0.]],       [[0., 0.],        [0., 0.],        [0., 0.],        [0., 0.]],       [[0., 0.],        [0., 0.],        [0., 0.],        [0., 0.]],       [[0., 0.],        [0., 0.],        [0., 0.],        [0., 0.]],       [[0., 0.],        [0., 0.],        [0., 0.],        [0., 0.]],       [[0., 0.],        [0., 0.],        [0., 0.],        [0., 0.]]], dtype=float32)>.

import tensorflow as tf

node_id_range = tf.constant(1, shape=[2], dtype=tf.int32)
stats_summary_list = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
l1 = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
l2 = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
tree_complexity = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
min_node_weight = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
max_splits = tf.constant(0, shape=[7,4,2], dtype=tf.float32)
tf.raw_ops.BoostedTreesCalculateBestGainsPerFeature(node_id_range=node_id_range, stats_summary_list=stats_summary_list, l1=l1, l2=l2, tree_complexity=tree_complexity, min_node_weight=min_node_weight, max_splits=max_splits)