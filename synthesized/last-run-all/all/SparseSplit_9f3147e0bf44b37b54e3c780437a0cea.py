import tensorflow as tf

split_dim = tf.constant(1250999896764, shape=[19,22,10], dtype=tf.int64)
indices = tf.constant([], shape=[0], dtype=tf.int64)
values = tf.constant(-1879048192, shape=[], dtype=tf.int64)
shape = tf.constant(1250999896764, shape=[], dtype=tf.int64)
tf.raw_ops.SparseSplit(split_dim=split_dim, indices=indices, values=values, shape=shape)