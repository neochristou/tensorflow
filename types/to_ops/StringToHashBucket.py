# LegacyStringToHashBucketOp

import tensorflow as tf

num_buckets = 10
string_tensor = tf.constant("a", shape=[3], dtype=tf.string)
tf.raw_ops.StringToHashBucket(string_tensor=string_tensor, num_buckets=num_buckets)
