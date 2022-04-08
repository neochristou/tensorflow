# DepthToSpaceOp

import tensorflow as tf

block_size = 2
data_format = "NHWC"
input = tf.constant(0, shape=[7,5,8,20], dtype=tf.float32)
tf.raw_ops.DepthToSpace(input=input, block_size=block_size, data_format=data_format)
