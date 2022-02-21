import tensorflow as tf

logits = tf.constant(-1.20397282, shape=[1,2], dtype=tf.float32)
num_samples = tf.constant(1879048192, shape=[], dtype=tf.int32)
seed = tf.constant(1987023866, shape=[2], dtype=tf.int64)
tf.raw_ops.StatelessMultinomial(logits=logits, num_samples=num_samples, seed=seed)