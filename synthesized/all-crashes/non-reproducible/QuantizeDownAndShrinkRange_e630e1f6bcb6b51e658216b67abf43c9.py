#   File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/QuantizeDownAndShrinkRange_e630e1f6bcb6b51e658216b67abf43c9.py", line 6    input = tf.constant(?, shape=[3], dtype=tf.qint32)                        ^SyntaxError: invalid syntax

# QuantizeDownAndShrinkRangeOp

import tensorflow as tf

out_type = tf.quint8
input = tf.constant(?, shape=[3], dtype=tf.qint32)
input_min = tf.constant([], shape=[0], dtype=tf.float32)
input_max = tf.constant(-256, shape=[1], dtype=tf.float32)
tf.raw_ops.QuantizeDownAndShrinkRange(input=input, input_min=input_min, input_max=input_max, out_type=out_type)
