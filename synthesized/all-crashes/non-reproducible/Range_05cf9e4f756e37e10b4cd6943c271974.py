# 2022-04-07 20:02:54.592412: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:54.594535: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/Range_05cf9e4f756e37e10b4cd6943c271974.py", line 8, in <module>    tf.raw_ops.Range(start=start, limit=limit, delta=delta)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_math_ops.py", line 7360, in _range    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: start must be a scalar, not shape [10,19,22] [Op:Range]

# RangeOp

import tensorflow as tf

start = tf.constant(-1879048192, shape=[10,19,22], dtype=tf.int32)
limit = tf.constant(1879048192, shape=[22,19,5,13], dtype=tf.int32)
delta = tf.constant(1879048192, shape=[22,19,5,13], dtype=tf.int32)
tf.raw_ops.Range(start=start, limit=limit, delta=delta)
