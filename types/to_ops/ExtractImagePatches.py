# ExtractImagePatchesOp

import tensorflow as tf

ksizes = [1, 1, 1, 1]
strides = [1, 1, 1, 1]
rates = [1, 1, 1, 1]
padding = "VALID"
images = tf.constant(?, shape=[2,3,4,5], dtype=tf.complex64)
tf.raw_ops.ExtractImagePatches(images=images, ksizes=ksizes, strides=strides, rates=rates, padding=padding)
