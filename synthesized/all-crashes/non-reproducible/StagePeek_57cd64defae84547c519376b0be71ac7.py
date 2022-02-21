# 2022-02-15 18:04:27.331988: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/StagePeek_57cd64defae84547c519376b0be71ac7.py", line 4, in <module>    tf.raw_ops.StagePeek(index=index)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: stage_peek() missing 1 required positional argument: 'dtypes'

import tensorflow as tf

index = tf.constant(-536870912, shape=[], dtype=tf.int32)
tf.raw_ops.StagePeek(index=index, dtypes=[tf.int32])
