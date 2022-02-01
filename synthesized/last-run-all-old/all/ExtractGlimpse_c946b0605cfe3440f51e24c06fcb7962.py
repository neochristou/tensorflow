import tensorflow as tf

input = tf.constant(123, shape=[1,61,41,1], dtype=tf.float32)
size = tf.constant(-536870912, shape=[2], dtype=tf.int32)
offsets = tf.constant(123, shape=[1,61,41,1], dtype=tf.float32)
tf.raw_ops.ExtractGlimpse(input=input, size=size, offsets=offsets)