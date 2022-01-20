import tensorflow as tf

arg_0 = tf.constant(0, shape=[3,2], dtype=tf.int64)
arg_1 = tf.constant("a", shape=[3], dtype=tf.string)
arg_2 = tf.constant(-1879048192, shape=[2], dtype=tf.int64)
tf.raw_ops.SerializeManySparse(sparse_indices=arg_0, sparse_values=arg_1, sparse_shape=arg_2)