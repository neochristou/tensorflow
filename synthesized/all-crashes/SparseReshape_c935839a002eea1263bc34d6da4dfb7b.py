import tensorflow as tf

arg_0 = tf.constant([], shape=[0,1], dtype=tf.int64)
arg_1 = tf.constant(-1879048192, shape=[1], dtype=tf.int64)
arg_2 = tf.constant(0, shape=[1], dtype=tf.int64)
tf.raw_ops.SparseReshape(input_indices=arg_0, input_shape=arg_1, new_shape=arg_2)