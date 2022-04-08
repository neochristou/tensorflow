# MatrixBandPartOp

import tensorflow as tf

input = tf.constant(.49671415301123267-0, shape=[3,1,1], dtype=tf.float64)
num_lower = tf.constant(-1, shape=[], dtype=tf.int32)
num_upper = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.BatchMatrixBandPart(input=input, num_lower=num_lower, num_upper=num_upper)
