# 2022-03-07 18:55:26.035758: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/RaggedRange_0344a221c4f1951c721190a0a37c8cb7.py", line 9, in <module>    tf.raw_ops.RaggedRange(starts=starts, limits=limits, deltas=deltas, Tsplits=Tsplits)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_ragged_math_ops.py", line 73, in ragged_range    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Requires delta != 0 [Op:RaggedRange]

# RaggedRangeOp

import tensorflow as tf

Tsplits = tf.int64
starts = tf.constant([-1879048192,-1879048192], shape=[2], dtype=tf.int64)
limits = tf.constant([0,2], shape=[2], dtype=tf.int64)
deltas = tf.constant([0,2], shape=[2], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=starts, limits=limits, deltas=deltas, Tsplits=Tsplits)