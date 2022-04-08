# GetKeyCounterOp

import tensorflow as tf

seed = tf.constant([1,2], shape=[2], dtype=tf.int32)
tf.raw_ops.StatelessRandomGetKeyCounter(seed=seed)
