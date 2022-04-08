# SelectV2Op

import tensorflow as tf

condition = tf.constant(True, shape=[4], dtype=tf.bool)
t = tf.constant(1, shape=[4], dtype=tf.int32)
e = tf.constant(-1, shape=[], dtype=tf.int32)
tf.raw_ops.SelectV2(condition=condition, t=t, e=e)
