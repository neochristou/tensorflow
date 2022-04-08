# 2022-04-07 20:03:14.586953: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:14.589089: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/StatelessParameterizedTruncatedNormal_7b29d369aeb8db1dc398c2ea5f33276d.py", line 11, in <module>    tf.raw_ops.StatelessParameterizedTruncatedNormal(shape=shape, seed=seed, means=means, stddevs=stddevs, minvals=minvals, maxvals=maxvals)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_stateless_random_ops.py", line 130, in stateless_parameterized_truncated_normal    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Invalid parameters [Op:StatelessParameterizedTruncatedNormal]

# StatelessParameterizedTruncatedNormal

import tensorflow as tf

shape = tf.constant(100000, shape=[1], dtype=tf.int32)
seed = tf.constant([-536870912,-536870912], shape=[2], dtype=tf.int32)
means = tf.constant(0, shape=[], dtype=tf.float32)
stddevs = tf.constant(0, shape=[], dtype=tf.float32)
minvals = tf.constant(0, shape=[], dtype=tf.float32)
maxvals = tf.constant(1, shape=[], dtype=tf.float32)
tf.raw_ops.StatelessParameterizedTruncatedNormal(shape=shape, seed=seed, means=means, stddevs=stddevs, minvals=minvals, maxvals=maxvals)
