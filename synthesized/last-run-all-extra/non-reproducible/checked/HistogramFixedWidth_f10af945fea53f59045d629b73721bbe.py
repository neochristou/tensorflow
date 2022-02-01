# Allocator
# 2022-01-31 11:00:19.264689: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/HistogramFixedWidth_f10af945fea53f59045d629b73721bbe.py", line 6, in <module>    tf.raw_ops.HistogramFixedWidth(values=values, value_range=value_range, nbins=nbins)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_math_ops.py", line 4127, in _histogram_fixed_width    _ops.raise_from_not_ok_status(e, name)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: value_range should satisfy value_range[0] < value_range[1], but got '[0, 0]' [Op:HistogramFixedWidth]

import tensorflow as tf

values = tf.constant([], shape=[0], dtype=tf.float64)
value_range = tf.constant([0, 5], shape=[2], dtype=tf.float64)
nbins = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.HistogramFixedWidth(
    values=values, value_range=value_range, nbins=nbins)
