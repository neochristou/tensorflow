# FakeQuantWithMinMaxVarsPerChannelOp

import tensorflow as tf

num_bits = 8
narrow_range = False
inputs = tf.constant(-3.5e+35, shape=[10,19,22], dtype=tf.float32)
min = tf.constant(3.5e+35, shape=[22,19,5,13], dtype=tf.float32)
max = tf.constant(3.5e+35, shape=[22,19,5,13], dtype=tf.float32)
tf.raw_ops.FakeQuantWithMinMaxVarsPerChannel(inputs=inputs, min=min, max=max, num_bits=num_bits, narrow_range=narrow_range)
