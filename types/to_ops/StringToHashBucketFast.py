# StringToHashBucketOp

import tensorflow as tf

num_buckets = 10
input = tf.constant("a", shape=[4], dtype=tf.string)
tf.raw_ops.StringToHashBucketFast(input=input, num_buckets=num_buckets)
