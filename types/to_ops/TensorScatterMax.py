# TensorScatterOp

import tensorflow as tf

tensor = tf.constant(1, shape=[8], dtype=tf.int32)
indices = tf.constant(431, shape=[4,1], dtype=tf.int32)
updates = tf.constant(9, shape=[4], dtype=tf.int32)
tf.raw_ops.TensorScatterMax(tensor=tensor, indices=indices, updates=updates)
