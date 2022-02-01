# 2022-01-31 11:00:43.573164: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/UnicodeEncode_a4c73f8ce6d798aab0a82d4aa96b4470.py", line 5, in <module>    tf.raw_ops.UnicodeEncode(input_values=input_values, input_splits=input_splits)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: unicode_encode() missing 1 required positional argument: 'output_encoding'

import tensorflow as tf

input_values = tf.constant([], shape=[0], dtype=tf.int32)
input_splits = tf.constant(0, shape=[5], dtype=tf.int64)
tf.raw_ops.UnicodeEncode(input_values=input_values, input_splits=input_splits)