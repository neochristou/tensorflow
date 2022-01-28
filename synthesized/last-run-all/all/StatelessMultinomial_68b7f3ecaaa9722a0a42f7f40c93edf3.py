import tensorflow as tf

logits = tf.constant(-3.5e+35, shape=[1,3], dtype=tf.float32)
num_samples = tf.constant(-3.5e+35, shape=[1,3], dtype=tf.float32)
seed = tf.constant(1879048192, shape=[], dtype=tf.int32)
output_dtype = tf.constant(1879048192, shape=[], dtype=tf.int32)
name = tf.constant(-1250999896764, shape=[2], dtype=tf.int64)
tf.raw_ops.StatelessMultinomial(logits=logits, num_samples=num_samples, seed=seed, output_dtype=output_dtype, name=name)