import tensorflow as tf

input_sizes = tf.constant(1879048192, shape=[13], dtype=tf.int32)
filter = tf.constant(0.184634328, shape=[1,1,48,2], dtype=tf.float32)
out_backprop = tf.constant(0.184634328, shape=[1,1,48,2], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropInput(input_sizes=input_sizes, filter=filter, out_backprop=out_backprop)