# CrossOp

import tensorflow as tf

a = tf.constant(-0.522, shape=[2,3], dtype=tf.float32)
b = tf.constant(1, shape=[2,3], dtype=tf.float32)
tf.raw_ops.Cross(a=a, b=b)
