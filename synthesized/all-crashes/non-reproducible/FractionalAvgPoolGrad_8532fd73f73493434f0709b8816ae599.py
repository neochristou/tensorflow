# 2022-04-07 20:01:37.561708: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:37.563652: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/FractionalAvgPoolGrad_8532fd73f73493434f0709b8816ae599.py", line 10, in <module>    tf.raw_ops.FractionalAvgPoolGrad(orig_input_tensor_shape=orig_input_tensor_shape, out_backprop=out_backprop, row_pooling_sequence=row_pooling_sequence, col_pooling_sequence=col_pooling_sequence, overlapping=overlapping)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_nn_ops.py", line 3255, in fractional_avg_pool_grad    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Given out_backprop shape [], row_seq_tensor must have at least 61469 elements, but got 4 [Op:FractionalAvgPoolGrad]

# FractionalAvgPoolGradOp

import tensorflow as tf

overlapping = True
orig_input_tensor_shape = tf.constant(-1879048192, shape=[4], dtype=tf.int64)
out_backprop = tf.constant(0, shape=[], dtype=tf.float64)
row_pooling_sequence = tf.constant(1, shape=[4], dtype=tf.int64)
col_pooling_sequence = tf.constant(1, shape=[4], dtype=tf.int64)
tf.raw_ops.FractionalAvgPoolGrad(orig_input_tensor_shape=orig_input_tensor_shape, out_backprop=out_backprop, row_pooling_sequence=row_pooling_sequence, col_pooling_sequence=col_pooling_sequence, overlapping=overlapping)
