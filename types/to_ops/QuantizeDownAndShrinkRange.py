# QuantizeDownAndShrinkRangeOp

import tensorflow as tf

out_type = tf.quint8
input = tf.constant(?, shape=[3], dtype=tf.qint32)
input_min = tf.constant(-256, shape=[1], dtype=tf.float32)
input_max = tf.constant(256, shape=[1], dtype=tf.float32)
tf.raw_ops.QuantizeDownAndShrinkRange(input=input, input_min=input_min, input_max=input_max, out_type=out_type)
