# ExtractVolumePatchesOp

import tensorflow as tf

ksizes = [1, 5, 5, 5, 1]
strides = [1, 1, 1, 1, 1]
padding = "SAME"
input = tf.constant(.184634332179032020, shape=[4,8,32,32,1], dtype=tf.float64)
tf.raw_ops.ExtractVolumePatches(input=input, ksizes=ksizes, strides=strides, padding=padding)
