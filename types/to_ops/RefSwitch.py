# SwitchOp

import tensorflow as tf

data = tf.constant(1, shape=[4], dtype=tf.int32)
pred = tf.constant(True, shape=[], dtype=tf.bool)
tf.raw_ops.RefSwitch(data=data, pred=pred)
