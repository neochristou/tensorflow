# 2022-01-20 07:04:24.341010: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:04:24.343124: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/LoadAndRemapMatrix_3e63b36849c6cb41394da77a26504e21.py", line 8, in <module>    tf.raw_ops.LoadAndRemapMatrix(ckpt_path=arg_0, old_tensor_name=arg_1, row_remapping=arg_2, col_remapping=arg_3, initializing_values=arg_4)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: load_and_remap_matrix() missing 2 required positional arguments: 'num_rows' and 'num_cols'

import tensorflow as tf

arg_0 = tf.constant("/tmp/checkpoint_ops_testakdh6w_l/bundle_checkpoint", shape=[1], dtype=tf.string)
arg_1 = tf.constant("/tmp/checkpoint_ops_testakdh6w_l/bundle_checkpoint", shape=[1], dtype=tf.string)
arg_2 = tf.constant(0, shape=[], dtype=tf.int64)
arg_3 = tf.constant(-1, shape=[7], dtype=tf.int64)
arg_4 = tf.constant(42, shape=[112], dtype=tf.float32)
tf.raw_ops.LoadAndRemapMatrix(ckpt_path=arg_0, old_tensor_name=arg_1, row_remapping=arg_2, col_remapping=arg_3, initializing_values=arg_4)