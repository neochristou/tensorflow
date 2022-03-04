import tensorflow as tf

key = tf.constant(-1250999896764, shape=[], dtype=tf.int64)
indices = tf.constant(0, shape=[1], dtype=tf.int32)
values = tf.constant(0, shape=[1], dtype=tf.int32)
tf.raw_ops.MapStageOp(key=key, indices=indices, values=values)