# LinSpaceOp

import tensorflow as tf

start = tf.constant(-3.5e+35, shape=[], dtype=tf.float32)
stop = tf.constant(3, shape=[], dtype=tf.float32)
num = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.LinSpace(start=start, stop=stop, num=num)
