import tensorflow as tf

arg_0 = tf.constant(0, shape=[4,3], dtype=tf.int64)
arg_1 = tf.constant(0, shape=[4,3], dtype=tf.int64)
arg_2 = tf.constant("a0", shape=[4], dtype=tf.string)
arg_3 = tf.constant("a0", shape=[4], dtype=tf.string)
arg_4 = tf.constant(-1250999896764, shape=[3], dtype=tf.int64)
tf.raw_ops.SparseConcat(indices=arg_0, values=arg_1, shapes=arg_2, concat_dim=arg_3, name=arg_4)