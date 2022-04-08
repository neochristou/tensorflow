# WhereCPUOp

import tensorflow as tf

condition = tf.constant(True, shape=[1], dtype=tf.bool)
tf.raw_ops.Where(condition=condition)
