# 2022-01-20 07:05:24.562865: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:05:24.565103: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/RaggedTensorToVariant_d6fc554b58b17a9ef34244f462782eb6.py", line 5, in <module>    tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=arg_0, rt_dense_values=arg_1)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: ragged_tensor_to_variant() missing 1 required positional argument: 'batched_input'

import tensorflow as tf

arg_0 = tf.constant(0, shape=[], dtype=tf.int64)
arg_1 = tf.constant(1, shape=[3], dtype=tf.int32)
tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=arg_0, rt_dense_values=arg_1)