#   File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/Requantize_cb18150f33036d112e89be6bd723143d.py", line 6    input = tf.constant(?, shape=[3], dtype=tf.qint32)                        ^SyntaxError: invalid syntax

# RequantizeOp

import tensorflow as tf

out_type = tf.quint8
input = tf.constant(?, shape=[3], dtype=tf.qint32)
input_min = tf.constant([], shape=[0], dtype=tf.float32)
input_max = tf.constant(-256, shape=[1], dtype=tf.float32)
requested_output_min = tf.constant(-256, shape=[1], dtype=tf.float32)
requested_output_max = tf.constant(-256, shape=[1], dtype=tf.float32)
tf.raw_ops.Requantize(input=input, input_min=input_min, input_max=input_max, requested_output_min=requested_output_min, requested_output_max=requested_output_max, out_type=out_type)
