import tensorflow as tf

arg_0 = tf.constant(0, shape=[10,3], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float32)
arg_2 = tf.constant(8608480567731124087, shape=[], dtype=tf.int64)
tf.raw_ops.SerializeManySparse(sparse_indices=arg_0, sparse_values=arg_1, sparse_shape=arg_2)