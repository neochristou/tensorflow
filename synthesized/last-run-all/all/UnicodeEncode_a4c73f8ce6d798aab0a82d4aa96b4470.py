import tensorflow as tf

input_values = tf.constant([], shape=[0], dtype=tf.int32)
input_splits = tf.constant(0, shape=[5], dtype=tf.int64)
tf.raw_ops.UnicodeEncode(input_values=input_values, input_splits=input_splits)