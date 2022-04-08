# UpperBoundOp

import tensorflow as tf

out_type = tf.int32
sorted_inputs = tf.constant(0, shape=[1,6], dtype=tf.float32)
values = tf.constant(0.04, shape=[1,9], dtype=tf.float32)
tf.raw_ops.UpperBound(sorted_inputs=sorted_inputs, values=values, out_type=out_type)
