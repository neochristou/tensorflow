# 2022-02-15 18:04:03.656450: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/MapStage_5f8e8f3833623716e4a436fca7b46a28.py", line 6, in <module>    tf.raw_ops.MapStage(key=key, indices=indices, values=values)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: map_stage() missing 1 required positional argument: 'dtypes'

import tensorflow as tf

key = tf.constant(-1250999896764, shape=[], dtype=tf.int64)
indices = tf.constant(0, shape=[1], dtype=tf.int32)
values = tf.constant(0, shape=[1], dtype=tf.int32)
tf.raw_ops.MapStage(key=key, indices=indices, values=values)