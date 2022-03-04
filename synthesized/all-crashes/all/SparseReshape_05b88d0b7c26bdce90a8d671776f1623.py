import tensorflow as tf

input_indices = tf.constant(0, shape=[3,2], dtype=tf.int64)
input_shape = tf.constant(-1879048192, shape=[2], dtype=tf.int64)
new_shape = tf.constant(2, shape=[2], dtype=tf.int64)
tf.raw_ops.SparseReshapeOp(input_indices=input_indices, input_shape=input_shape, new_shape=new_shape)