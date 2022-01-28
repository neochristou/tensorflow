import tensorflow as tf

input = tf.constant(-64992, shape=[2,5,4,3,2], dtype=tf.float16)
filter = tf.constant(0, shape=[], dtype=tf.int32)
out_backprop = tf.constant(0, shape=[2,5,4,3,2], dtype=tf.float16)
tf.raw_ops.Conv3DBackpropFilter(input=input, filter=filter, out_backprop=out_backprop)