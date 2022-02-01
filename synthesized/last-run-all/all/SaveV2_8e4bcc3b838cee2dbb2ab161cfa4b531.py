import tensorflow as tf

prefix = tf.constant("-1_temp/part", shape=[], dtype=tf.string)
tensor_names = tf.constant("-1_temp/part", shape=[], dtype=tf.string)
shape_and_slices = tf.constant("-1_temp/part", shape=[], dtype=tf.string)
tf.raw_ops.SaveV2(prefix=prefix, tensor_names=tensor_names, shape_and_slices=shape_and_slices)