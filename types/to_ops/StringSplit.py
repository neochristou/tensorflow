# StringSplitOp

import tensorflow as tf

skip_empty = False
input = tf.constant("hello", shape=[1], dtype=tf.string)
delimiter = tf.constant("[]", shape=[], dtype=tf.string)
tf.raw_ops.StringSplit(input=input, delimiter=delimiter, skip_empty=skip_empty)
