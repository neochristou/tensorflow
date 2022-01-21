import tensorflow as tf

arg_0 = tf.constant(-3.5e+35, shape=[1,2], dtype=tf.float32)
arg_1 = tf.constant(1879048192, shape=[], dtype=tf.int32)
arg_2 = tf.constant(2025741188, shape=[2], dtype=tf.int64)
tf.raw_ops.StatelessMultinomial(logits=arg_0, num_samples=arg_1, seed=arg_2)