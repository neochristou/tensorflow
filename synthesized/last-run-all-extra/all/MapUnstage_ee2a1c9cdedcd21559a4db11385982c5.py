import tensorflow as tf

key = tf.constant(-1879048192, shape=[], dtype=tf.int64)
indices = tf.constant(0, shape=[2], dtype=tf.int32)
tf.raw_ops.MapUnstage(key=key, indices=indices)