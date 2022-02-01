# 2022-01-31 11:00:33.153309: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/SaveV2_8e4bcc3b838cee2dbb2ab161cfa4b531.py", line 6, in <module>    tf.raw_ops.SaveV2(prefix=prefix, tensor_names=tensor_names, shape_and_slices=shape_and_slices)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: save_v2() missing 1 required positional argument: 'tensors'

import tensorflow as tf

prefix = tf.constant("-1_temp/part", shape=[], dtype=tf.string)
tensor_names = tf.constant("-1_temp/part", shape=[], dtype=tf.string)
shape_and_slices = tf.constant("-1_temp/part", shape=[], dtype=tf.string)
tf.raw_ops.SaveV2(prefix=prefix, tensor_names=tensor_names, shape_and_slices=shape_and_slices)