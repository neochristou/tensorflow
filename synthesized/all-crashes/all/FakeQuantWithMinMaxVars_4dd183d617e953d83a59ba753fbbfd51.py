import tensorflow as tf

arg_0 = tf.constant(0, shape=[], dtype=tf.float32)
arg_1 = tf.constant(0, shape=[2,3], dtype=tf.float32)
arg_2 = tf.constant(0, shape=[2,3], dtype=tf.float32)
tf.raw_ops.FakeQuantWithMinMaxVars(inputs=arg_0, min=arg_1, max=arg_2)