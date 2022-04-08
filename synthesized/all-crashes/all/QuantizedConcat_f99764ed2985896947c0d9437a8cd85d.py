# QuantizedConcatOp

import tensorflow as tf

concat_dim = tf.constant(0, shape=[], dtype=tf.int32)
values = tf.constant(?, shape=[2,2,3], dtype=tf.qint32)
input_mins = tf.constant(?, shape=[2,2,3], dtype=tf.qint32)
input_maxes = tf.constant([], shape=[0], dtype=tf.float32)
tf.raw_ops.QuantizedConcat(concat_dim=concat_dim, values=values, input_mins=input_mins, input_maxes=input_maxes)
