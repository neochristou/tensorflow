# ParseTensorOp

import tensorflow as tf

out_type = tf.uint16
serialized = tf.constant("bogus", shape=[], dtype=tf.string)
tf.raw_ops.ParseTensor(serialized=serialized, out_type=out_type)
