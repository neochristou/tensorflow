# SliceOp

import tensorflow as tf

input = tf.constant(-0.808016658, shape=[16,64], dtype=tf.float32)
begin = tf.constant([0,32], shape=[2], dtype=tf.int32)
size = tf.constant([16,32], shape=[2], dtype=tf.int32)
tf.raw_ops.Slice(input=input, begin=begin, size=size)
