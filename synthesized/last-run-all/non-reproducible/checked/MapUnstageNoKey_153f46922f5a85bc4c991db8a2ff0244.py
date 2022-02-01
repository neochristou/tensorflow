# 2022-01-31 21:30:29.259361: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/MapUnstageNoKey_153f46922f5a85bc4c991db8a2ff0244.py", line 4, in <module>    tf.raw_ops.MapUnstageNoKey(indices=indices)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: map_unstage_no_key() missing 1 required positional argument: 'dtypes'

import tensorflow as tf

indices = tf.constant(-536870912, shape=[1], dtype=tf.int32)
tf.raw_ops.MapUnstageNoKey(indices=indices)