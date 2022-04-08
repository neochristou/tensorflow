# SparseTensorDenseMatMulOp

import tensorflow as tf

adjoint_a = False
adjoint_b = False
a_indices = tf.constant(1, shape=[3,2], dtype=tf.int64)
a_values = tf.constant(0, shape=[3], dtype=tf.float32)
a_shape = tf.constant([4,5], shape=[2], dtype=tf.int64)
b = tf.constant(111, shape=[5,1], dtype=tf.float32)
tf.raw_ops.SparseTensorDenseMatMul(a_indices=a_indices, a_values=a_values, a_shape=a_shape, b=b, adjoint_a=adjoint_a, adjoint_b=adjoint_b)
