# ScaleAndTranslateOp

import tensorflow as tf

kernel_type = "triangle"
antialias = False
images = tf.constant(643232, shape=[1,3,2,1], dtype=tf.float32)
size = tf.constant([6,4], shape=[2], dtype=tf.int32)
scale = tf.constant([2,2], shape=[2], dtype=tf.float32)
translation = tf.constant([0,0], shape=[2], dtype=tf.float32)
tf.raw_ops.ScaleAndTranslate(images=images, size=size, scale=scale, translation=translation, kernel_type=kernel_type, antialias=antialias)
