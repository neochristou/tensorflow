# BatchToSpaceNDOp

import tensorflow as tf

input = tf.constant(0, shape=[20,5,8,7], dtype=tf.float32)
block_shape = tf.constant([2,2], shape=[2], dtype=tf.int64)
crops = tf.constant(0, shape=[2,2], dtype=tf.int64)
tf.raw_ops.BatchToSpaceND(input=input, block_shape=block_shape, crops=crops)
