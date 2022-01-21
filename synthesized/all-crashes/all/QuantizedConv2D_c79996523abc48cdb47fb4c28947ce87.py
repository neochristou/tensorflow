import tensorflow as tf

arg_0 = tf.constant(1, shape=[1,2,3,3], dtype=tf.quint8)
arg_1 = tf.constant(1, shape=[1,2,3,3], dtype=tf.quint8)
arg_2 = tf.constant([], shape=[0], dtype=tf.float32)
arg_3 = tf.constant(0, shape=[], dtype=tf.float32)
arg_4 = tf.constant(0, shape=[], dtype=tf.float32)
arg_5 = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.QuantizedConv2D(input=arg_0, filter=arg_1, min_input=arg_2, max_input=arg_3, min_filter=arg_4, max_filter=arg_5)