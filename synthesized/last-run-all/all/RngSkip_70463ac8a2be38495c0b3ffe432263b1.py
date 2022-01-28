import tensorflow as tf

resource = tf.constant(1, shape=[], dtype=tf.int32)
tf.raw_ops.RngSkip(resource=resource)