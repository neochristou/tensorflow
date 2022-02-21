# 2022-02-15 18:04:06.749563: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/ParameterizedTruncatedNormal_cd2587cf0ca595a1aa225233f4f29e4d.py", line 8, in <module>    tf.raw_ops.ParameterizedTruncatedNormal(shape=shape, means=means, stdevs=stdevs, minvals=minvals, maxvals=maxvals)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_random_ops.py", line 151, in parameterized_truncated_normal    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Invalid parameters [Op:ParameterizedTruncatedNormal]

import tensorflow as tf

shape = tf.constant(100000, shape=[1], dtype=tf.int32)
means = tf.constant(-3.5e+35, shape=[], dtype=tf.float32)
stdevs = tf.constant(-3.5e+35, shape=[], dtype=tf.float32)
minvals = tf.constant(1, shape=[], dtype=tf.float32)
maxvals = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.ParameterizedTruncatedNormal(shape=shape, means=means, stdevs=stdevs, minvals=minvals, maxvals=maxvals)