# PadOp

import tensorflow as tf

input = tf.constant(1, shape=[2,2], dtype=tf.float32)
paddings = tf.constant(1, shape=[2,2], dtype=tf.int32)
tf.raw_ops.PadV2(input=input, paddings=paddings)
