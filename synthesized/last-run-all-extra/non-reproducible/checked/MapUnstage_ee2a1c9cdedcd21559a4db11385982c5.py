# 2022-01-31 11:00:24.589774: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/MapUnstage_ee2a1c9cdedcd21559a4db11385982c5.py", line 5, in <module>    tf.raw_ops.MapUnstage(key=key, indices=indices)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: map_unstage() missing 1 required positional argument: 'dtypes'

import tensorflow as tf

key = tf.constant(-1879048192, shape=[], dtype=tf.int64)
indices = tf.constant(0, shape=[2], dtype=tf.int32)
tf.raw_ops.MapUnstage(key=key, indices=indices, dtypes=[tf.int64, tf.int32])
