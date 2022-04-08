# StatelessRandomOp

import tensorflow as tf

dtype = tf.int32
shape = tf.constant(3, shape=[1], dtype=tf.int32)
seed = tf.constant(10413732777507651514, shape=[1], dtype=tf.uint64)
tf.raw_ops.StatelessTruncatedNormal(shape=shape, seed=seed, dtype=dtype)
