# ReshapeOp

import tensorflow as tf

tensor = tf.constant(1, shape=[], dtype=tf.float32)
shape = tf.constant(1, shape=[4], dtype=tf.int32)
tf.raw_ops.Reshape(tensor=tensor, shape=shape)
