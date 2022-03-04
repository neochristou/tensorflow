import tensorflow as tf

indices = tf.constant(-1879048192, shape=[5,2], dtype=tf.int64)
values = tf.constant(0, shape=[5], dtype=tf.int64)
dense_shape = tf.constant(0, shape=[5,2], dtype=tf.int64)
weights = tf.constant(0, shape=[5], dtype=tf.int64)
tf.raw_ops.SparseCountSparseOutput(indices=indices, values=values, dense_shape=dense_shape, weights=weights)