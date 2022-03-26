# StatelessMultinomialOp

import tensorflow as tf

output_dtype = tf.int64
logits = tf.constant(-3.5e+35, shape=[1,2], dtype=tf.float32)
num_samples = tf.constant(1879048192, shape=[], dtype=tf.int32)
seed = tf.constant([2489719881,3666025645], shape=[2], dtype=tf.int64)
tf.raw_ops.StatelessMultinomial(logits=logits, num_samples=num_samples, seed=seed, output_dtype=output_dtype)