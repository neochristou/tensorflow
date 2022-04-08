# CheckNumericsOp

import tensorflow as tf

message = "Input is not a number."
tensor = tf.constant(nan, shape=[5,4], dtype=tf.float32)
tf.raw_ops.CheckNumerics(tensor=tensor, message=message)
