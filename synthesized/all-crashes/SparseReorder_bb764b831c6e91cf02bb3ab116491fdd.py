import tensorflow as tf

arg_0 = tf.constant(-1879048192, shape=[2,2], dtype=tf.int64)
arg_1 = tf.constant(3, shape=[2], dtype=tf.float32)
arg_2 = tf.constant(-1250999896764, shape=[2], dtype=tf.int64)
tf.raw_ops.SparseReorder(input_indices=arg_0, input_values=arg_1, input_shape=arg_2)