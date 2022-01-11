import tensorflow as tf

arg_0 = tf.constant([], shape=[0,2], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0,2], dtype=tf.int64)
arg_2 = tf.constant([], shape=[0,2], dtype=tf.int64)
arg_3 = tf.constant("[]", shape=[0], dtype=tf.string)
arg_4 = tf.constant("[]", shape=[0], dtype=tf.string)
arg_5 = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.SparseCrossV2(indices=arg_0, values=arg_1, shapes=arg_2, dense_inputs=arg_3, sep=arg_4, name=arg_5)