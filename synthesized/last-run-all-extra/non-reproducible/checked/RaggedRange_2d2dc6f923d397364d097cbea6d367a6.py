# Wrong type
# 2022-01-31 11:00:29.858979: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/RaggedRange_2d2dc6f923d397364d097cbea6d367a6.py", line 6, in <module>    tf.raw_ops.RaggedRange(starts=starts, limits=limits, deltas=deltas)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_ragged_math_ops.py", line 73, in ragged_range    _ops.raise_from_not_ok_status(e, name)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Requires delta != 0 [Op:RaggedRange]

import tensorflow as tf

starts = tf.constant(-1879048192, shape=[], dtype=tf.int64)
limits = tf.constant(0, shape=[5], dtype=tf.int64)
deltas = tf.constant(0, shape=[5], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=starts, limits=limits, deltas=deltas)
