# StringToNumberOp

import tensorflow as tf

out_type = tf.float64
string_tensor = tf.constant("0", shape=[1], dtype=tf.string)
tf.raw_ops.StringToNumber(string_tensor=string_tensor, out_type=out_type)
