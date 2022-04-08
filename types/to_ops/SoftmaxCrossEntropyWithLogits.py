# SoftmaxXentWithLogitsOp

import tensorflow as tf

features = tf.constant(1, shape=[2,4], dtype=tf.float32)
labels = tf.constant(1.2, shape=[2,4], dtype=tf.float32)
tf.raw_ops.SoftmaxCrossEntropyWithLogits(features=features, labels=labels)
