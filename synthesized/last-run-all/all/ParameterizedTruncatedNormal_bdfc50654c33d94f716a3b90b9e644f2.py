import tensorflow as tf

shape = tf.constant(100000, shape=[1], dtype=tf.int32)
means = tf.constant(-2, shape=[], dtype=tf.float32)
stdevs = tf.constant(0, shape=[], dtype=tf.float32)
minvals = tf.constant(0, shape=[], dtype=tf.float32)
maxvals = tf.constant(1, shape=[], dtype=tf.float32)
tf.raw_ops.ParameterizedTruncatedNormal(shape=shape, means=means, stdevs=stdevs, minvals=minvals, maxvals=maxvals)