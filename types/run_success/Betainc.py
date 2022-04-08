# BetaincOp

import tensorflow as tf

a = tf.constant(1.84634328, shape=[30,40,50], dtype=tf.float32)
b = tf.constant(7.39165401, shape=[30,40,50], dtype=tf.float32)
x = tf.constant(0.813053906, shape=[30,40,50], dtype=tf.float32)
tf.raw_ops.Betainc(a=a, b=b, x=x)
