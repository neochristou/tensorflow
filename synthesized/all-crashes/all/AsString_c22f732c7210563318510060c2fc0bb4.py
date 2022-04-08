# AsStringOp

import tensorflow as tf

precision = -1
scientific = False
shortest = False
width = -1
fill = ""
input = tf.constant(False, shape=[], dtype=tf.bool)
tf.raw_ops.AsString(input=input, precision=precision, scientific=scientific, shortest=shortest, width=width, fill=fill)
