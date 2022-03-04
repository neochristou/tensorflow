import tensorflow as tf

input = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
filter_sizes = tf.constant(0, shape=[], dtype=tf.int32)
out_backprop = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
tf.raw_ops.Conv3DBackpropFilterV2(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop)