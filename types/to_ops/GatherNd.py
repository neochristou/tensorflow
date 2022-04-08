# GatherNdOp

import tensorflow as tf

params = tf.constant(1, shape=[2,2], dtype=tf.float16)
indices = tf.constant(0, shape=[2,2], dtype=tf.int32)
tf.raw_ops.GatherNd(params=params, indices=indices)
