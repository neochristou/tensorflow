# QuantizedReluOp

import tensorflow as tf

out_type = tf.quint8
features = tf.constant(28, shape=[4,2], dtype=tf.quint8)
min_features = tf.constant([], shape=[0], dtype=tf.float32)
max_features = tf.constant(-128, shape=[1], dtype=tf.float32)
tf.raw_ops.QuantizedRelu(features=features, min_features=min_features, max_features=max_features, out_type=out_type)
