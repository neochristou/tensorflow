# 2022-01-31 11:00:20.359043: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/LoadAndRemapMatrix_116bd318ae5645d6e9a0f2c415989efa.py", line 8, in <module>    tf.raw_ops.LoadAndRemapMatrix(ckpt_path=ckpt_path, old_tensor_name=old_tensor_name, row_remapping=row_remapping, col_remapping=col_remapping, initializing_values=initializing_values)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: load_and_remap_matrix() missing 2 required positional arguments: 'num_rows' and 'num_cols'

import tensorflow as tf

ckpt_path = tf.constant(
    "/tmp/warm_starting_util_test1t7fu1yy/tmp4zivjml4/model-0", shape=[], dtype=tf.string)
old_tensor_name = tf.constant(
    "/tmp/warm_starting_util_test1t7fu1yy/tmp4zivjml4/model-0", shape=[], dtype=tf.string)
row_remapping = tf.constant(0, shape=[], dtype=tf.int64)
col_remapping = tf.constant(3, shape=[3], dtype=tf.int64)
initializing_values = tf.constant([], shape=[0, 1], dtype=tf.float32)
tf.raw_ops.LoadAndRemapMatrix(ckpt_path=ckpt_path, old_tensor_name=old_tensor_name, row_remapping=row_remapping,
                              col_remapping=col_remapping, initializing_values=initializing_values, num_rows=1, num_cols=1)
