import tensorflow as tf

arg_0 = tf.constant(2.3, shape=[6], dtype=tf.float32)
arg_1 = tf.constant(1.2, shape=[6], dtype=tf.float32)
arg_2 = tf.constant(1.2, shape=[6], dtype=tf.float32)
arg_3 = tf.constant(1.2, shape=[6], dtype=tf.float32)
tf.raw_ops.BoostedTreesMakeQuantileSummaries(float_values=arg_0, example_weights=arg_1, epsilon=arg_2, name=arg_3)