# UnpackOp

import tensorflow as tf

num = 3
axis = 0
value = tf.constant(100, shape=[3], dtype=tf.int64)
tf.raw_ops.Unpack(value=value, num=num, axis=axis)
