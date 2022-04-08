# ScanOp

import tensorflow as tf

exclusive = True
reverse = False
x = tf.constant(?, shape=[4,1], dtype=tf.complex64)
axis = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.CumulativeLogsumexp(x=x, axis=axis, exclusive=exclusive, reverse=reverse)
