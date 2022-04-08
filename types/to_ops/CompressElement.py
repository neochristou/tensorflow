# CompressElementOp

import tensorflow as tf

components = tf.constant(2, shape=[], dtype=tf.int32)
tf.raw_ops.CompressElement(components=components)
