import tensorflow as tf

input = tf.constant(0, shape=[], dtype=tf.bool)
tf.raw_ops.AsString(input=input)