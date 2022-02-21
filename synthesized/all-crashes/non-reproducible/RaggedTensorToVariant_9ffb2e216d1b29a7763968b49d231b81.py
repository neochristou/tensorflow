# 2022-02-15 18:04:10.416692: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/RaggedTensorToVariant_9ffb2e216d1b29a7763968b49d231b81.py", line 5, in <module>    tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: ragged_tensor_to_variant() missing 1 required positional argument: 'batched_input'

import tensorflow as tf

rt_nested_splits = tf.constant(-8608480567731124087, shape=[], dtype=tf.int64)
rt_dense_values = tf.constant(0, shape=[7], dtype=tf.int64)
tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values)