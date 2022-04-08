# StringUpperOp

import tensorflow as tf

encoding = ""
input = tf.constant("a", shape=[], dtype=tf.string)
tf.raw_ops.StringUpper(input=input, encoding=encoding)
