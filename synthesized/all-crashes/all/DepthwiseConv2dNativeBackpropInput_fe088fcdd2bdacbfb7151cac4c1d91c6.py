import tensorflow as tf

arg_0 = tf.constant(1879048192, shape=[13], dtype=tf.int32)
arg_1 = tf.constant(.068289727-0, shape=[3,3,3,1], dtype=tf.float32)
arg_2 = tf.constant(.068289727-0, shape=[3,3,3,1], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropInput(input_sizes=arg_0, filter=arg_1, out_backprop=arg_2)