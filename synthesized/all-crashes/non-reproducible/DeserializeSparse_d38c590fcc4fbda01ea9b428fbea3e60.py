# 2022-02-15 18:03:53.541618: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/DeserializeSparse_d38c590fcc4fbda01ea9b428fbea3e60.py", line 4, in <module>    tf.raw_ops.DeserializeSparse(serialized_sparse=serialized_sparse)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: deserialize_sparse() missing 1 required positional argument: 'dtype'

import tensorflow as tf

serialized_sparse = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.DeserializeSparse(serialized_sparse=serialized_sparse)