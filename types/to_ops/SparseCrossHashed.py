# SparseCrossHashedOp

import tensorflow as tf

indices = tf.constant(0, shape=[3,2], dtype=tf.int64)
values = tf.constant(0, shape=[1,2], dtype=tf.int64)
shapes = tf.constant(0, shape=[2,2], dtype=tf.int64)
dense_inputs = tf.constant("-FC1", shape=[3], dtype=tf.string)
num_buckets = tf.constant("-FC2", shape=[1], dtype=tf.string)
strong_hash = tf.constant("[batch1-FC3-F1,batch1-FC3-F2]", shape=[2], dtype=tf.string)
salt = tf.constant([1,3], shape=[2], dtype=tf.int64)
tf.raw_ops.SparseCrossHashed(indices=indices, values=values, shapes=shapes, dense_inputs=dense_inputs, num_buckets=num_buckets, strong_hash=strong_hash, salt=salt)
