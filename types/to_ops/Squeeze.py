# SqueezeOp

import tensorflow as tf

input = tf.constant(True, shape=[], dtype=tf.bool)
tf.raw_ops.Squeeze(input=input)
