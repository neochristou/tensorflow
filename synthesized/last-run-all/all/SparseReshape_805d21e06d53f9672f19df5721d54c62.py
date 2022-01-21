import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[3,2], dtype=tf.int64)
arg_1 = tf.constant(-1879048192, shape=[2], dtype=tf.int64)
arg_2 = tf.constant(2, shape=[2], dtype=tf.int64)
tf.raw_ops.SparseReshape(input_indices=arg_0, input_shape=arg_1, new_shape=arg_2)