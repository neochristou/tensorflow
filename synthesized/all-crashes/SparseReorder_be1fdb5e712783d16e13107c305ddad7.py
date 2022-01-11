import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[6,2], dtype=tf.int64)
arg_1 = tf.constant(1.5e+300, shape=[24,30], dtype=tf.float64)
arg_2 = tf.constant(5, shape=[2], dtype=tf.int64)
tf.raw_ops.SparseReorder(input_indices=arg_0, input_values=arg_1, input_shape=arg_2)