import tensorflow as tf

arg_0 = tf.constant([], shape=[0], dtype=tf.float32)
arg_1 = tf.constant(65534, shape=[12,10,19], dtype=tf.int32)
tf.raw_ops.MirrorPad(input=arg_0, paddings=arg_1)