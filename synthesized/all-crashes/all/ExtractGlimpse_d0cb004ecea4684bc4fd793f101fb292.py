import tensorflow as tf

arg_0 = tf.constant(-3.5e+35, shape=[1,61,41,1], dtype=tf.float32)
arg_1 = tf.constant(-536870912, shape=[2], dtype=tf.int32)
arg_2 = tf.constant(123, shape=[1,61,41,1], dtype=tf.float32)
tf.raw_ops.ExtractGlimpse(input=arg_0, size=arg_1, offsets=arg_2)