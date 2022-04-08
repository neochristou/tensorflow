# SparseConcatOp

import tensorflow as tf

concat_dim = 1
indices = tf.constant(0, shape=[4,3], dtype=tf.int64)
values = tf.constant(0, shape=[6,3], dtype=tf.int64)
shapes = tf.constant("a0", shape=[4], dtype=tf.string)
tf.raw_ops.SparseConcat(indices=indices, values=values, shapes=shapes, concat_dim=concat_dim)
