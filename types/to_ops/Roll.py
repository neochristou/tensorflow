# RollOp

import tensorflow as tf

input = tf.constant(?, shape=[1,6], dtype=tf.complex128)
shift = tf.constant(-1, shape=[], dtype=tf.int32)
axis = tf.constant(-1, shape=[], dtype=tf.int32)
tf.raw_ops.Roll(input=input, shift=shift, axis=axis)
