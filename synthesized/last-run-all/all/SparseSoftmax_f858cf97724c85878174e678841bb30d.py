import tensorflow as tf

arg_0 = tf.constant(0, shape=[72,3], dtype=tf.int64)
arg_1 = tf.constant(0.301107913, shape=[72], dtype=tf.float32)
arg_2 = tf.constant(-1250999896764, shape=[3], dtype=tf.int64)
tf.raw_ops.SparseSoftmax(sp_indices=arg_0, sp_values=arg_1, sp_shape=arg_2)