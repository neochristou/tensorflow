# 2022-03-07 18:55:27.283304: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/RaggedTensorToVariant_8f34bba2a5c500fa6817c1c6bd7033fc.py", line 8, in <module>    tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, batched_input=batched_input)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_ragged_conversion_ops.py", line 400, in ragged_tensor_to_variant    return ragged_tensor_to_variant_eager_fallback(  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_ragged_conversion_ops.py", line 433, in ragged_tensor_to_variant_eager_fallback    raise TypeError(TypeError: Expected list for 'rt_nested_splits' argument to 'ragged_tensor_to_variant' Op, not <tf.Tensor: shape=(), dtype=int64, numpy=-8608480567731124087>.

# RaggedTensorToVariantOp

import tensorflow as tf

batched_input = True
rt_nested_splits = tf.constant(-8608480567731124087, shape=[], dtype=tf.int64)
rt_dense_values = tf.constant(0, shape=[7], dtype=tf.int64)
tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, batched_input=batched_input)