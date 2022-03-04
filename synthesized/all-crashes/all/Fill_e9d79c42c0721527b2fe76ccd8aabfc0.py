import tensorflow as tf

dims = tf.constant(1879048192, shape=[], dtype=tf.int32)
value = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.FillOp(dims=dims, value=value)