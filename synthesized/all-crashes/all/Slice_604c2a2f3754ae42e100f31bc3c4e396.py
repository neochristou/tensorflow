import tensorflow as tf

input = tf.constant(-536870912, shape=[1], dtype=tf.int32)
begin = tf.constant(-536870912, shape=[1], dtype=tf.int32)
size = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.Slice(input=input, begin=begin, size=size)