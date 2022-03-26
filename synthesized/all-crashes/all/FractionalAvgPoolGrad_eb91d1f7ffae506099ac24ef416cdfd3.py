# FractionalAvgPoolGradOp

import tensorflow as tf

overlapping = True
orig_input_tensor_shape = tf.constant(-1879048192, shape=[4], dtype=tf.int64)
out_backprop = tf.constant([], shape=[0], dtype=tf.float64)
row_pooling_sequence = tf.constant(1, shape=[4], dtype=tf.int64)
col_pooling_sequence = tf.constant(1, shape=[4], dtype=tf.int64)
tf.raw_ops.FractionalAvgPoolGrad(orig_input_tensor_shape=orig_input_tensor_shape, out_backprop=out_backprop, row_pooling_sequence=row_pooling_sequence, col_pooling_sequence=col_pooling_sequence, overlapping=overlapping)