# BucketizeOp

import tensorflow as tf

boundaries = [0, 3, 8, 11]
input = tf.constant(-5, shape=[2,5], dtype=tf.int32)
tf.raw_ops.Bucketize(input=input, boundaries=boundaries)
