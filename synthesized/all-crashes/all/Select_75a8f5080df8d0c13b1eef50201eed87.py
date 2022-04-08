# SelectOp

import tensorflow as tf

condition = tf.constant(False, shape=[], dtype=tf.bool)
x = tf.constant(3.5e+35, shape=[13,24], dtype=tf.float32)
y = tf.constant(-3.5e+35, shape=[18,22,19,5], dtype=tf.float32)
tf.raw_ops.Select(condition=condition, x=x, y=y)
