# BiasOp

import tensorflow as tf

value = tf.constant(0.0446744, shape=[3,40], dtype=tf.float32)
bias = tf.constant(0, shape=[40], dtype=tf.float32)
tf.raw_ops.BiasAddV1(value=value, bias=bias)
