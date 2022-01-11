import tensorflow as tf

arg_0 = tf.constant(-3.5e+35, shape=[10,19,22], dtype=tf.float32)
arg_1 = tf.constant(3.5e+35, shape=[22,19,5,13], dtype=tf.float32)
arg_2 = tf.constant(3.5e+35, shape=[22,19,5,13], dtype=tf.float32)
tf.raw_ops.FakeQuantWithMinMaxVarsPerChannel(inputs=arg_0, min=arg_1, max=arg_2)