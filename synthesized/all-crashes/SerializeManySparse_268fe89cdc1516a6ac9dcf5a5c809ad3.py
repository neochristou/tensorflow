import tensorflow as tf

arg_0 = tf.constant(0, shape=[6,2], dtype=tf.int64)
arg_1 = tf.constant(1, shape=[6], dtype=tf.float32)
arg_2 = tf.constant(-1879048192, shape=[13], dtype=tf.int64)
tf.raw_ops.SerializeManySparse(sparse_indices=arg_0, sparse_values=arg_1, sparse_shape=arg_2)