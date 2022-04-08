# AddNOp

import tensorflow as tf

inputs = tf.constant(0, shape=[5,5,5,5], dtype=tf.float32)
tf.raw_ops.AddN(inputs=inputs)
