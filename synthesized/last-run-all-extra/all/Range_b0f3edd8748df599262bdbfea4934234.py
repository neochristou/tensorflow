import tensorflow as tf

start = tf.constant(-1250999896764, shape=[], dtype=tf.int64)
limit = tf.constant(1, shape=[], dtype=tf.int64)
delta = tf.constant(1, shape=[], dtype=tf.int64)
tf.raw_ops.Range(start=start, limit=limit, delta=delta)