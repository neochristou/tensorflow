# ShardedFilenameOp

import tensorflow as tf

basename = tf.constant("/tmp/extension_type_teste8qs34a3mb8f30j4/variables/variables_temp/part", shape=[], dtype=tf.string)
shard = tf.constant(0, shape=[], dtype=tf.int32)
num_shards = tf.constant(1, shape=[], dtype=tf.int32)
tf.raw_ops.ShardedFilename(basename=basename, shard=shard, num_shards=num_shards)
