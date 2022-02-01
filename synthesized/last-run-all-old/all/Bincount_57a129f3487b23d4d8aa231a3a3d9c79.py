import tensorflow as tf

arr = tf.constant(0, shape=[1], dtype=tf.int32)
size = tf.constant(536870912, shape=[], dtype=tf.int32)
weights = tf.constant([], shape=[0], dtype=tf.int64)
tf.raw_ops.Bincount(arr=arr, size=size, weights=weights)