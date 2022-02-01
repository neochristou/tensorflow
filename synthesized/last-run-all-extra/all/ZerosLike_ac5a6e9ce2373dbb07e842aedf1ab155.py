import tensorflow as tf

x = tf.constant(3.5e+35, shape=[12,18,22,19], dtype=tf.float32)
tf.raw_ops.ZerosLike(x=x)