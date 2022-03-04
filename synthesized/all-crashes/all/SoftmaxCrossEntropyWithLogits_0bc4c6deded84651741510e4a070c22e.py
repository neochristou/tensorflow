import tensorflow as tf

features = tf.constant(0, shape=[], dtype=tf.float32)
labels = tf.constant(1, shape=[8,3], dtype=tf.float32)
tf.raw_ops.SoftmaxXentWithLogitsOp(features=features, labels=labels)