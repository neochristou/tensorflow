# SoftmaxOp

import tensorflow as tf

logits = tf.constant(-6.30731344, shape=[4,9], dtype=tf.float32)
tf.raw_ops.LogSoftmax(logits=logits)
