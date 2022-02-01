# Wrong types
# 2022-01-31 11:00:42.486055: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/StatelessParameterizedTruncatedNormal_37b8b25403d640e0ebd6508721d7099d.py", line 9, in <module>    tf.raw_ops.StatelessParameterizedTruncatedNormal(shape=shape, seed=seed, means=means, stddevs=stddevs, minvals=minvals, maxvals=maxvals)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_stateless_random_ops.py", line 130, in stateless_parameterized_truncated_normal    _ops.raise_from_not_ok_status(e, name)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Invalid parameters [Op:StatelessParameterizedTruncatedNormal]

import tensorflow as tf

shape = tf.constant(100000, shape=[1], dtype=tf.int32)
seed = tf.constant(0, shape=[2], dtype=tf.int32)
means = tf.constant(0, shape=[], dtype=tf.float32)
stddevs = tf.constant(-2, shape=[], dtype=tf.float32)
minvals = tf.constant(1, shape=[], dtype=tf.float32)
maxvals = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.StatelessParameterizedTruncatedNormal(
    shape=shape, seed=seed, means=means, stddevs=stddevs, minvals=minvals, maxvals=maxvals)
