# 2022-02-15 18:04:59.879391: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/UnicodeEncode_6c3794a07584b61c1af4f20b30dbc29b.py", line 5, in <module>    tf.raw_ops.UnicodeEncode(input_values=input_values, input_splits=input_splits)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: unicode_encode() missing 1 required positional argument: 'output_encoding'

import tensorflow as tf

input_values = tf.constant([], shape=[0], dtype=tf.int32)
input_splits = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.UnicodeEncode(input_values=input_values, input_splits=input_splits)