# OptionalFromValueOp

import tensorflow as tf

components = tf.constant(17554184, shape=[1,10,10], dtype=tf.float32)
tf.raw_ops.OptionalFromValue(components=components)
