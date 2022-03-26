# 2022-03-26 16:56:41.345135: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/RaggedGather_708964555fed7143aab4fd01e9cbf97a.py", line 9, in <module>    tf.raw_ops.RaggedGather(params_nested_splits=params_nested_splits, params_dense_values=params_dense_values, indices=indices, OUTPUT_RAGGED_RANK=OUTPUT_RAGGED_RANK)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_ragged_array_ops.py", line 247, in ragged_gather    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Split tensors must not be scalars [Op:RaggedGather]

# RaggedGatherOp

import tensorflow as tf

OUTPUT_RAGGED_RANK = 2
params_nested_splits = tf.constant(0, shape=[5], dtype=tf.int64)
params_dense_values = tf.constant(1879048192, shape=[], dtype=tf.int64)
indices = tf.constant(-1879048192, shape=[7], dtype=tf.int32)
tf.raw_ops.RaggedGather(params_nested_splits=params_nested_splits, params_dense_values=params_dense_values, indices=indices, OUTPUT_RAGGED_RANK=OUTPUT_RAGGED_RANK)