# FillOp

import tensorflow as tf

dims = tf.constant(536870912, shape=[], dtype=tf.int32)
value = tf.constant(-3.5e+35, shape=[], dtype=tf.float32)
tf.raw_ops.Fill(dims=dims, value=value)