import tensorflow as tf

condition = tf.constant(0, shape=[], dtype=tf.bool)
x = tf.constant("[]", shape=[0], dtype=tf.string)
y = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.SelectOp(condition=condition, x=x, y=y)