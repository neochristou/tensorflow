import tensorflow as tf

arg_0 = tf.constant(-65534, shape=[], dtype=tf.int32)
arg_1 = tf.constant(0, shape=[], dtype=tf.int32)
arg_2 = tf.constant(-536870912, shape=[], dtype=tf.int32)
tf.raw_ops.While(input=arg_0, cond=arg_1, body=arg_2)