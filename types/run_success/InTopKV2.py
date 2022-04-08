# InTopK

import tensorflow as tf

predictions = tf.constant(0.1, shape=[2,4], dtype=tf.float32)
targets = tf.constant([2,4], shape=[2], dtype=tf.int32)
k = tf.constant(2, shape=[], dtype=tf.int32)
tf.raw_ops.InTopKV2(predictions=predictions, targets=targets, k=k)
