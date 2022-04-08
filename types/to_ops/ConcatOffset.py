# ConcatOffsetOp

import tensorflow as tf

concat_dim = tf.constant(1, shape=[], dtype=tf.int32)
shape = tf.constant([16,32], shape=[2], dtype=tf.int32)
tf.raw_ops.ConcatOffset(concat_dim=concat_dim, shape=shape)
