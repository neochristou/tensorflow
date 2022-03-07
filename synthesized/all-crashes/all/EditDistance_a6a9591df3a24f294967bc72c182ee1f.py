# EditDistanceOp

import tensorflow as tf

normalize = True
hypothesis_indices = tf.constant(-1250999896764, shape=[3,3], dtype=tf.int64)
hypothesis_values = tf.constant(0, shape=[3], dtype=tf.int64)
hypothesis_shape = tf.constant(0, shape=[3], dtype=tf.int64)
truth_indices = tf.constant(-1250999896764, shape=[3,3], dtype=tf.int64)
truth_values = tf.constant(2, shape=[3], dtype=tf.int64)
truth_shape = tf.constant(2, shape=[3], dtype=tf.int64)
tf.raw_ops.EditDistance(hypothesis_indices=hypothesis_indices, hypothesis_values=hypothesis_values, hypothesis_shape=hypothesis_shape, truth_indices=truth_indices, truth_values=truth_values, truth_shape=truth_shape, normalize=normalize)