# EmptyOp

import tensorflow as tf

dtype = tf.float32
init = True
shape = tf.constant(13, shape=[3], dtype=tf.int32)
tf.raw_ops.Empty(shape=shape, dtype=dtype, init=init)
