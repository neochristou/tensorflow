# SparseTensorToCSRSparseMatrixCPUOp

import tensorflow as tf

indices = tf.constant(0, shape=[31,2], dtype=tf.int64)
values = tf.constant(?, shape=[31], dtype=tf.complex64)
dense_shape = tf.constant([5,11], shape=[2], dtype=tf.int64)
tf.raw_ops.SparseTensorToCSRSparseMatrix(indices=indices, values=values, dense_shape=dense_shape)
