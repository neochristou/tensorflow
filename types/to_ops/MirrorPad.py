# MirrorPadOp

import tensorflow as tf

mode = "REFLECT"
input = tf.constant(?, shape=[2,5], dtype=tf.complex64)
paddings = tf.constant(1, shape=[2,2], dtype=tf.int32)
tf.raw_ops.MirrorPad(input=input, paddings=paddings, mode=mode)
