# 2022-03-07 19:08:48.060860: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory2022-03-07 19:08:48.060909: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.2022-03-07 19:08:48.991736: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory2022-03-07 19:08:48.991804: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)2022-03-07 19:08:48.991827: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (devel): /proc/driver/nvidia/version does not exist2022-03-07 19:08:48.992094: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/RaggedTensorToVariant_8f34bba2a5c500fa6817c1c6bd7033fc.py", line 8, in <module>    tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, batched_input=batched_input)  File "/home/neo/.local/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 400, in wrapper    return f(**kwargs)  File "/home/neo/.local/lib/python3.9/site-packages/tensorflow/python/ops/gen_ragged_conversion_ops.py", line 400, in ragged_tensor_to_variant    return ragged_tensor_to_variant_eager_fallback(  File "/home/neo/.local/lib/python3.9/site-packages/tensorflow/python/ops/gen_ragged_conversion_ops.py", line 433, in ragged_tensor_to_variant_eager_fallback    raise TypeError(TypeError: Expected list for 'rt_nested_splits' argument to 'ragged_tensor_to_variant' Op, not <tf.Tensor: shape=(), dtype=int64, numpy=-8608480567731124087>.

# RaggedTensorToVariantOp

import tensorflow as tf

batched_input = True
rt_nested_splits = tf.constant(-8608480567731124087, shape=[], dtype=tf.int64)
rt_dense_values = tf.constant(0, shape=[7], dtype=tf.int64)
tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, batched_input=batched_input)