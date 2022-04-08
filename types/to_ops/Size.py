# SizeOp

import tensorflow as tf

out_type = tf.int32
input = tf.constant(0.184634328, shape=[3,7], dtype=tf.float32)
tf.raw_ops.Size(input=input, out_type=out_type)
