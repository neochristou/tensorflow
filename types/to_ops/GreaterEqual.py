# BinaryOp

import tensorflow as tf

x = tf.constant(0.154919341, shape=[], dtype=tf.float32)
y = tf.constant(-0.154919341, shape=[], dtype=tf.float32)
tf.raw_ops.GreaterEqual(x=x, y=y)
