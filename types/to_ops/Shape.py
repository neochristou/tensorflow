# ShapeOp

import tensorflow as tf

out_type = tf.int32
input = tf.constant(25, shape=[3], dtype=tf.int32)
tf.raw_ops.Shape(input=input, out_type=out_type)
