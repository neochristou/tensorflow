import tensorflow as tf

arg_0 = tf.constant(1879048192, shape=[], dtype=tf.int32)
arg_1 = tf.constant([], shape=[0], dtype=tf.int32)
arg_2 = tf.constant(65534, shape=[], dtype=tf.int32)
tf.raw_ops.ScatterNd(indices=arg_0, updates=arg_1, shape=arg_2)