import tensorflow as tf

values = tf.constant([], shape=[0], dtype=tf.float64)
value_range = tf.constant(0, shape=[2], dtype=tf.float64)
nbins = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.HistogramFixedWidth(values=values, value_range=value_range, nbins=nbins)