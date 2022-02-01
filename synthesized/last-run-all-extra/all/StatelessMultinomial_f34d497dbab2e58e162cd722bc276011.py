import tensorflow as tf

logits = tf.constant(-3.5e+35, shape=[10,19,22], dtype=tf.float32)
num_samples = tf.constant(-536870912, shape=[], dtype=tf.int32)
seed = tf.constant(3852221141, shape=[2], dtype=tf.int64)
tf.raw_ops.StatelessMultinomial(logits=logits, num_samples=num_samples, seed=seed)