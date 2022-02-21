import tensorflow as tf

indices = tf.constant(-1250999896764, shape=[], dtype=tf.int64)
depth = tf.constant(1879048192, shape=[], dtype=tf.int32)
on_value = tf.constant(1, shape=[], dtype=tf.float32)
off_value = tf.constant(1, shape=[], dtype=tf.float32)
tf.raw_ops.OneHot(indices=indices, depth=depth, on_value=on_value, off_value=off_value)