# 2022-04-07 20:02:53.295008: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:53.296973: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/RaggedTensorToVariant_c2b9009a2e18e4979a88b895ba202f06.py", line 8, in <module>    tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, batched_input=batched_input)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_ragged_conversion_ops.py", line 400, in ragged_tensor_to_variant    return ragged_tensor_to_variant_eager_fallback(  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_ragged_conversion_ops.py", line 433, in ragged_tensor_to_variant_eager_fallback    raise TypeError(TypeError: Expected list for 'rt_nested_splits' argument to 'ragged_tensor_to_variant' Op, not <tf.Tensor: shape=(), dtype=int64, numpy=0>.

# RaggedTensorToVariantOp

import tensorflow as tf

batched_input = False
rt_nested_splits = tf.constant(0, shape=[], dtype=tf.int64)
rt_dense_values = tf.constant(203, shape=[3], dtype=tf.int32)
tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, batched_input=batched_input)
