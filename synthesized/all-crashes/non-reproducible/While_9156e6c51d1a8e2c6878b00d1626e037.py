# 2022-01-20 07:06:26.378757: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:06:26.380737: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/While_9156e6c51d1a8e2c6878b00d1626e037.py", line 6, in <module>    tf.raw_ops.While(input=arg_0, cond=arg_1, body=arg_2)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/ops/gen_functional_ops.py", line 1238, in _while    return _while_eager_fallback(  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/ops/gen_functional_ops.py", line 1285, in _while_eager_fallback    _attr_T, input = _execute.convert_to_mixed_eager_tensors(input, ctx)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/eager/execute.py", line 295, in convert_to_mixed_eager_tensors    v = [ops.convert_to_tensor(t, ctx=ctx) for t in values]  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 526, in __iter__    raise TypeError("Cannot iterate over a scalar tensor.")TypeError: Cannot iterate over a scalar tensor.

import tensorflow as tf

arg_0 = tf.constant(0, shape=[], dtype=tf.int32)
arg_1 = tf.constant(0, shape=[], dtype=tf.int32)
arg_2 = tf.constant(-536870912, shape=[], dtype=tf.int32)
tf.raw_ops.While(input=arg_0, cond=arg_1, body=arg_2)