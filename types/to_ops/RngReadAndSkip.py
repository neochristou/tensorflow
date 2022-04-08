# RngSkipOp

import tensorflow as tf

resource = tf.constant(1, shape=[], dtype=tf.int32)
alg = tf.constant(10, shape=[], dtype=tf.uint64)
tf.raw_ops.RngReadAndSkip(resource=resource, alg=alg)
