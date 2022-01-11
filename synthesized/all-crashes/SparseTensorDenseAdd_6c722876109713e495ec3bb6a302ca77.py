import tensorflow as tf

arg_0 = tf.constant(0, shape=[461,3], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float32)
arg_2 = tf.constant(10, shape=[3], dtype=tf.int64)
arg_3 = tf.constant(000, shape=[10,10,1], dtype=tf.float32)
tf.raw_ops.SparseTensorDenseAdd(a_indices=arg_0, a_values=arg_1, a_shape=arg_2, b=arg_3)