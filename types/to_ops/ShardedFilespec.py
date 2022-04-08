# ShardedFilespecOp

import tensorflow as tf

basename = tf.constant("foo", shape=[], dtype=tf.string)
num_shards = tf.constant(100, shape=[], dtype=tf.int32)
tf.raw_ops.ShardedFilespec(basename=basename, num_shards=num_shards)
