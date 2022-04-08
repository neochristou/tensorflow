# ShapeNOp

import tensorflow as tf

out_type = tf.int32
input = tf.constant(0.25109911, shape=[16,32], dtype=tf.float32)
tf.raw_ops.ShapeN(input=input, out_type=out_type)
