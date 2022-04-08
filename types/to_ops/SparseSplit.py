# SparseSplitOp

import tensorflow as tf

num_split = 3
split_dim = tf.constant(-3, shape=[], dtype=tf.int64)
indices = tf.constant(0, shape=[14,2], dtype=tf.int64)
values = tf.constant(0, shape=[14], dtype=tf.int64)
shape = tf.constant([4,6], shape=[2], dtype=tf.int64)
tf.raw_ops.SparseSplit(split_dim=split_dim, indices=indices, values=values, shape=shape, num_split=num_split)
