# StringToKeyedHashBucketOp

import tensorflow as tf

num_buckets = 10
key = [98765, 132]
input = tf.constant("a", shape=[3], dtype=tf.string)
tf.raw_ops.StringToHashBucketStrong(input=input, num_buckets=num_buckets, key=key)
