import tensorflow as tf

arg_0 = tf.constant(0, shape=[1024000,2], dtype=tf.int64)
arg_1 = tf.constant(1, shape=[1024000], dtype=tf.float32)
arg_2 = tf.constant(-1250999896764, shape=[2], dtype=tf.int64)
arg_3 = tf.constant(8193, shape=[2], dtype=tf.int64)
arg_4 = tf.constant(8193, shape=[2], dtype=tf.int64)
tf.raw_ops.SparseSlice(indices=arg_0, values=arg_1, shape=arg_2, start=arg_3, size=arg_4)