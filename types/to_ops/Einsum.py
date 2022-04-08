# EinsumOp

import tensorflow as tf

equation = ",->"
inputs = tf.constant(1.76405239, shape=[], dtype=tf.float32)
tf.raw_ops.Einsum(inputs=inputs, equation=equation)
