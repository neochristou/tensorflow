import tensorflow as tf

arg_0 = tf.constant(-8608480567731124087, shape=[], dtype=tf.int64)
arg_1 = tf.constant(0, shape=[5], dtype=tf.int64)
arg_2 = tf.constant(1, shape=[], dtype=tf.int64)
tf.raw_ops.RaggedRange(starts=arg_0, limits=arg_1, deltas=arg_2)