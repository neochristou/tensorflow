import tensorflow as tf

arg_0 = tf.constant(0, shape=[2,2], dtype=tf.int64)
arg_1 = tf.constant(1879048192, shape=[13], dtype=tf.int32)
arg_2 = tf.constant([], shape=[0], dtype=tf.int64)
tf.raw_ops.AddManySparseToTensorsMap(sparse_indices=arg_0, sparse_values=arg_1, sparse_shape=arg_2)