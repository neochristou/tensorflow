# FillOp

import tensorflow as tf

dims = tf.constant([1,384], shape=[2], dtype=tf.int32)
value = tf.constant(1, shape=[], dtype=tf.float32)
tf.raw_ops.Fill(dims=dims, value=value)
