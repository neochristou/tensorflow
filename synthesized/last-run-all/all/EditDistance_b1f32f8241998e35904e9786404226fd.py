import tensorflow as tf

arg_0 = tf.constant(-1250999896764, shape=[3,3], dtype=tf.int64)
arg_1 = tf.constant(0, shape=[3], dtype=tf.int64)
arg_2 = tf.constant(0, shape=[3], dtype=tf.int64)
arg_3 = tf.constant(0, shape=[2,3], dtype=tf.int64)
arg_4 = tf.constant(-1879048192, shape=[2], dtype=tf.int64)
arg_5 = tf.constant(2, shape=[3], dtype=tf.int64)
tf.raw_ops.EditDistance(hypothesis_indices=arg_0, hypothesis_values=arg_1, hypothesis_shape=arg_2, truth_indices=arg_3, truth_values=arg_4, truth_shape=arg_5)