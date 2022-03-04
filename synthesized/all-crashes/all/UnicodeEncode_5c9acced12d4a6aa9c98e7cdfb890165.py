import tensorflow as tf

input_values = tf.constant([], shape=[0], dtype=tf.int32)
input_splits = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.UnicodeEncodeOp(input_values=input_values, input_splits=input_splits)