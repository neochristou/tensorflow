# OneHotOp

import tensorflow as tf

axis = -1
indices = tf.constant(1, shape=[100,5], dtype=tf.int64)
depth = tf.constant(2, shape=[], dtype=tf.int32)
on_value = tf.constant(1, shape=[], dtype=tf.float32)
off_value = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.OneHot(indices=indices, depth=depth, on_value=on_value, off_value=off_value, axis=axis)
