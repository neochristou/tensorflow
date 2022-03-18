# StatefulMultinomialOp

import tensorflow as tf

seed = 10
seed2 = 15
output_dtype = tf.int64
logits = tf.constant(-3.5e+35, shape=[1,2], dtype=tf.float32)
num_samples = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.Multinomial(logits=logits, num_samples=num_samples, seed=seed, seed2=seed2, output_dtype=output_dtype)