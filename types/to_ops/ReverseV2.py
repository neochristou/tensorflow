# ReverseV2Op

import tensorflow as tf

tensor = tf.constant(.49671415301123267-0, shape=[3,1], dtype=tf.float64)
axis = tf.constant(1, shape=[1], dtype=tf.int32)
tf.raw_ops.ReverseV2(tensor=tensor, axis=axis)
