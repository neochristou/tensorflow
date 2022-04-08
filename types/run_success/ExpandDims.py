# ExpandDimsOp

import tensorflow as tf

input = tf.constant("-00000", shape=[], dtype=tf.string)
axis = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.ExpandDims(input=input, axis=axis)
