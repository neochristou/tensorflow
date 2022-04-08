# SparseCount

import tensorflow as tf

binary_output = False
minlength = 6
maxlength = 6
indices = tf.constant(1879048192, shape=[7], dtype=tf.int64)
values = tf.constant([], shape=[0], dtype=tf.int64)
dense_shape = tf.constant([], shape=[0], dtype=tf.int64)
weights = tf.constant([], shape=[0], dtype=tf.int64)
tf.raw_ops.SparseCountSparseOutput(indices=indices, values=values, dense_shape=dense_shape, weights=weights, binary_output=binary_output, minlength=minlength, maxlength=maxlength)
