# ExitOp

import tensorflow as tf

data = tf.constant(4, shape=[], dtype=tf.float32)
tf.raw_ops.RefExit(data=data)
