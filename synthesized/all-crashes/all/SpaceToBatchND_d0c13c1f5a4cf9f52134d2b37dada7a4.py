# SpaceToBatchNDOp

import tensorflow as tf

input = tf.constant(-3.5e+35, shape=[10,19,22], dtype=tf.float32)
block_shape = tf.constant(65534, shape=[], dtype=tf.int32)
paddings = tf.constant(0, shape=[2,2], dtype=tf.int32)
tf.raw_ops.SpaceToBatchND(input=input, block_shape=block_shape, paddings=paddings)