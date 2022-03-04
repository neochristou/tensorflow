import tensorflow as tf

input = tf.constant(1, shape=[2,6,8,6,2], dtype=tf.float32)
filter_sizes = tf.constant(0, shape=[], dtype=tf.int32)
out_backprop = tf.constant(1, shape=[2,6,8,6,2], dtype=tf.float32)
tf.raw_ops.Conv3DCustomBackpropFilterOp(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop)