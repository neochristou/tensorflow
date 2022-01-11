import tensorflow as tf

arg_0 = tf.constant(0, shape=[2,5,4,3,2], dtype=tf.float16)
arg_1 = tf.constant(0, shape=[], dtype=tf.int32)
arg_2 = tf.constant(0, shape=[2,5,4,3,2], dtype=tf.float16)
tf.raw_ops.Conv3DBackpropFilter(input=arg_0, filter=arg_1, out_backprop=arg_2)