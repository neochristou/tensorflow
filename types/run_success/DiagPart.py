# DiagPartOp

import tensorflow as tf

input = tf.constant(7, shape=[3,3], dtype=tf.float64)
tf.raw_ops.DiagPart(input=input)
