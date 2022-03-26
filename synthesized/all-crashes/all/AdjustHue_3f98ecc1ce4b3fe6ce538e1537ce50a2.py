# AdjustHueOp

import tensorflow as tf

images = tf.constant(0, shape=[2,2,3], dtype=tf.float32)
delta = tf.constant(-3.5e+35, shape=[], dtype=tf.float32)
tf.raw_ops.AdjustHue(images=images, delta=delta)