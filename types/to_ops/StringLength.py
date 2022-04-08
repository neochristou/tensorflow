# StringLengthOp

import tensorflow as tf

unit = "BYTE"
input = tf.constant("1", shape=[1,3,2], dtype=tf.string)
tf.raw_ops.StringLength(input=input, unit=unit)
