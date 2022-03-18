# HistogramFixedWidthOp

import tensorflow as tf

dtype = tf.int32
values = tf.constant(-1.5e+300, shape=[6], dtype=tf.float64)
value_range = tf.constant([0,5], shape=[2], dtype=tf.float64)
nbins = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.HistogramFixedWidth(values=values, value_range=value_range, nbins=nbins, dtype=dtype)