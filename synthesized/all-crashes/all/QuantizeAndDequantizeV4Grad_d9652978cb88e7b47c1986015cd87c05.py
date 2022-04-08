# QuantizeAndDequantizeV4GradientOp

import tensorflow as tf

axis = -1
gradients = tf.constant(1, shape=[2,2], dtype=tf.float64)
input = tf.constant(1, shape=[2,2], dtype=tf.float64)
input_min = tf.constant([], shape=[0], dtype=tf.float64)
input_max = tf.constant(-10, shape=[], dtype=tf.float64)
tf.raw_ops.QuantizeAndDequantizeV4Grad(gradients=gradients, input=input, input_min=input_min, input_max=input_max, axis=axis)
