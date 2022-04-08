# SparseSoftmaxXentWithLogitsOp

import tensorflow as tf

features = tf.constant(-1.60943794, shape=[15,4], dtype=tf.float32)
labels = tf.constant(0, shape=[15], dtype=tf.int32)
tf.raw_ops.SparseSoftmaxCrossEntropyWithLogits(features=features, labels=labels)
