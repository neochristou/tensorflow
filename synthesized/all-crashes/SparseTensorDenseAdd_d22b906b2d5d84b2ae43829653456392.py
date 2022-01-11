import tensorflow as tf

arg_0 = tf.constant(0, shape=[17,2], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float32)
arg_2 = tf.constant(6, shape=[2], dtype=tf.int64)
arg_3 = tf.constant(-0.223668531, shape=[6,12], dtype=tf.float32)
tf.raw_ops.SparseTensorDenseAdd(a_indices=arg_0, a_values=arg_1, a_shape=arg_2, b=arg_3)