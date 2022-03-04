import tensorflow as tf

indices = tf.constant(53, shape=[3], dtype=tf.int64)
values = tf.constant(0.554979503, shape=[218650], dtype=tf.float32)
dense_shape = tf.constant(53, shape=[3], dtype=tf.int64)
tf.raw_ops.SparseTensorToCSRSparseMatrix(indices=indices, values=values, dense_shape=dense_shape)