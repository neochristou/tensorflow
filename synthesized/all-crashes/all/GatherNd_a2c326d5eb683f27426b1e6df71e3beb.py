import tensorflow as tf

arg_0 = tf.constant(0, shape=[5], dtype=tf.float32)
arg_1 = tf.constant([], shape=[0], dtype=tf.float64)
tf.raw_ops.GatherNd(params=arg_0, indices=arg_1)