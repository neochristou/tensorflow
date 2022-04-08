# TileOp

import tensorflow as tf

input = tf.constant(1, shape=[1,1,1,1], dtype=tf.float32)
multiples = tf.constant(1, shape=[4], dtype=tf.int32)
tf.raw_ops.Tile(input=input, multiples=multiples)
