# SparseTensorDenseAddOp

import tensorflow as tf

a_indices = tf.constant(0, shape=[461,3], dtype=tf.int64)
a_values = tf.constant(1.60516, shape=[461], dtype=tf.float32)
a_shape = tf.constant(10, shape=[3], dtype=tf.int64)
b = tf.constant(00, shape=[10,10,1], dtype=tf.float32)
tf.raw_ops.SparseTensorDenseAdd(a_indices=a_indices, a_values=a_values, a_shape=a_shape, b=b)
