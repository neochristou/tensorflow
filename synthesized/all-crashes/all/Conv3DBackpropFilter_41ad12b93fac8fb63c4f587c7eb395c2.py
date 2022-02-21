import tensorflow as tf

input = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
filter = tf.constant(0, shape=[], dtype=tf.int32)
out_backprop = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
tf.raw_ops.Conv3DBackpropFilter(input=input, filter=filter, out_backprop=out_backprop)