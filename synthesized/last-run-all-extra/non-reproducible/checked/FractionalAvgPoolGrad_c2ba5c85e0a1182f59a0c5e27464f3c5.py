# Wrong type
# 2022-01-31 11:00:16.148999: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/FractionalAvgPoolGrad_c2ba5c85e0a1182f59a0c5e27464f3c5.py", line 7, in <module>    tf.raw_ops.FractionalAvgPoolGrad(orig_input_tensor_shape=orig_input_tensor_shape, out_backprop=out_backprop, row_pooling_sequence=row_pooling_sequence, col_pooling_sequence=col_pooling_sequence)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_nn_ops.py", line 3255, in fractional_avg_pool_grad    _ops.raise_from_not_ok_status(e, name)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Given out_backprop shape [0], row_seq_tensor must have at least 19257 elements, but got 4 [Op:FractionalAvgPoolGrad]

import tensorflow as tf

orig_input_tensor_shape = tf.constant(-1879048192, shape=[4], dtype=tf.int64)
out_backprop = tf.constant([], shape=[0], dtype=tf.float64)
row_pooling_sequence = tf.constant(1, shape=[4], dtype=tf.int64)
col_pooling_sequence = tf.constant(1, shape=[4], dtype=tf.int64)
tf.raw_ops.FractionalAvgPoolGrad(orig_input_tensor_shape=orig_input_tensor_shape, out_backprop=out_backprop,
                                 row_pooling_sequence=row_pooling_sequence, col_pooling_sequence=col_pooling_sequence)
