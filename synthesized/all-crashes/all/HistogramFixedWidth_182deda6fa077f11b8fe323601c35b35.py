import tensorflow as tf

arg_0 = tf.constant(1.5e+300, shape=[13], dtype=tf.float64)
arg_1 = tf.constant(0, shape=[2], dtype=tf.float64)
arg_2 = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.HistogramFixedWidth(values=arg_0, value_range=arg_1, nbins=arg_2)