import tensorflow as tf

indices = tf.constant(0, shape=[6,2], dtype=tf.int64)
values = tf.constant([], shape=[0], dtype=tf.int32)
shape = tf.constant(-1250999896764, shape=[2], dtype=tf.int64)
start = tf.constant(4, shape=[2], dtype=tf.int64)
size = tf.constant(4, shape=[2], dtype=tf.int64)
tf.raw_ops.SparseSlice(indices=indices, values=values, shape=shape, start=start, size=size)