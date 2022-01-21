import tensorflow as tf

arg_0 = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
arg_1 = tf.constant(0, shape=[], dtype=tf.int32)
arg_2 = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
tf.raw_ops.Conv3DBackpropFilter(input=arg_0, filter=arg_1, out_backprop=arg_2)