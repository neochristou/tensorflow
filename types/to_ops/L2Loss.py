# L2LossOp

import tensorflow as tf

t = tf.constant([1,-2], shape=[2], dtype=tf.float32)
tf.raw_ops.L2Loss(t=t)
