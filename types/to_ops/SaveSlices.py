# SaveSlicesOp

import tensorflow as tf

filename = tf.constant("/tmp/saver_large_variable_testdgvly_xg/tmpxzrbrwfm/large_variable", shape=[], dtype=tf.string)
tensor_names = tf.constant("Variable", shape=[1], dtype=tf.string)
shapes_and_slices = tf.constant("[]", shape=[1], dtype=tf.string)
data = tf.constant(False, shape=[2,1024,1024,1024], dtype=tf.bool)
tf.raw_ops.SaveSlices(filename=filename, tensor_names=tensor_names, shapes_and_slices=shapes_and_slices, data=data)
