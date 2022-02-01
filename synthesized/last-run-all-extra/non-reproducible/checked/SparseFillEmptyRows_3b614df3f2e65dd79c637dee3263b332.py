# Wrong type
# 2022-01-31 11:00:35.329386: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/SparseFillEmptyRows_3b614df3f2e65dd79c637dee3263b332.py", line 7, in <module>    tf.raw_ops.SparseFillEmptyRows(indices=indices, values=values, dense_shape=dense_shape, default_value=default_value)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_sparse_ops.py", line 1744, in sparse_fill_empty_rows    _ops.raise_from_not_ok_status(e, name)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: dense_shape must be a vector, saw: [19,22,10] [Op:SparseFillEmptyRows]

import tensorflow as tf

indices = tf.constant(-1879048192, shape=[5], dtype=tf.int64)
values = tf.constant(0, shape=[], dtype=tf.int64)
dense_shape = tf.constant(1250999896764, shape=[19, 22, 10], dtype=tf.int64)
default_value = tf.constant(-8608480567731124087, shape=[], dtype=tf.int64)
tf.raw_ops.SparseFillEmptyRows(
    indices=indices, values=values, dense_shape=dense_shape, default_value=default_value)
