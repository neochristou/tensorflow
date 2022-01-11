import tensorflow as tf

arg_0 = tf.constant(?, shape=[2,5], dtype=tf.complex64)
arg_1 = tf.constant(0, shape=[2,2], dtype=tf.int32)
tf.raw_ops.MirrorPad(input=arg_0, paddings=arg_1)