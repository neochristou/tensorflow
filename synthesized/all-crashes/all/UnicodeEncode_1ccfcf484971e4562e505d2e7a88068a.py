# UnicodeEncodeOp

import tensorflow as tf

output_encoding = "UTF-8"
errors = "strict"
replacement_char = 65533
input_values = tf.constant([], shape=[0], dtype=tf.int32)
input_splits = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.UnicodeEncode(input_values=input_values, input_splits=input_splits, output_encoding=output_encoding, errors=errors, replacement_char=replacement_char)