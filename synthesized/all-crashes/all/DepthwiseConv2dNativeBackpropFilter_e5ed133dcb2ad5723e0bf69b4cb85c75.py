import tensorflow as tf

arg_0 = tf.constant(0.184634328, shape=[4,5,5,48], dtype=tf.float32)
arg_1 = tf.constant(1879048192, shape=[13], dtype=tf.int32)
arg_2 = tf.constant(0.184634328, shape=[4,5,5,48], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropFilter(input=arg_0, filter_sizes=arg_1, out_backprop=arg_2)