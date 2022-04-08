# SparseSliceOp

import tensorflow as tf

indices = tf.constant(0, shape=[1024000,2], dtype=tf.int64)
values = tf.constant(1, shape=[1024000], dtype=tf.float64)
shape = tf.constant([8193,1024000], shape=[2], dtype=tf.int64)
start = tf.constant([1,0], shape=[2], dtype=tf.int64)
size = tf.constant([8192,1024000], shape=[2], dtype=tf.int64)
tf.raw_ops.SparseSlice(indices=indices, values=values, shape=shape, start=start, size=size)
