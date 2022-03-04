import tensorflow as tf

logits = tf.constant(-3.5e+35, shape=[1,2], dtype=tf.float32)
num_samples = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.Multinomial(logits=logits, num_samples=num_samples)