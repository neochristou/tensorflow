import tensorflow as tf

arg_0 = tf.constant([], shape=[0], dtype=tf.float64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float32)
arg_2 = tf.constant(243, shape=[6,1], dtype=tf.int32)
tf.raw_ops.ScatterNd(indices=arg_0, updates=arg_1, shape=arg_2)