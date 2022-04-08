# SubstrOp

import tensorflow as tf

unit = "BYTE"
input = tf.constant("ten", shape=[4,3], dtype=tf.string)
pos = tf.constant(1, shape=[3], dtype=tf.int32)
len = tf.constant(1, shape=[3], dtype=tf.int32)
tf.raw_ops.Substr(input=input, pos=pos, len=len, unit=unit)
