# BiasGradOp

import tensorflow as tf

data_format = "NHWC"
out_backprop = tf.constant(-5.49433707e, shape=[2,12], dtype=tf.float32)
tf.raw_ops.BiasAddGrad(out_backprop=out_backprop, data_format=data_format)
