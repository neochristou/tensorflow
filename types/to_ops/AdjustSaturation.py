# AdjustSaturationOp

import tensorflow as tf

images = tf.constant(0.58937192, shape=[2,4,4,3], dtype=tf.float32)
scale = tf.constant(0.1, shape=[], dtype=tf.float32)
tf.raw_ops.AdjustSaturation(images=images, scale=scale)
