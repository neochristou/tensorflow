# DynamicPartitionOp

import tensorflow as tf

num_partitions = 16
data = tf.constant(0.554979513497522, shape=[3072], dtype=tf.float64)
partitions = tf.constant(0, shape=[3072], dtype=tf.int32)
tf.raw_ops.DynamicPartition(data=data, partitions=partitions, num_partitions=num_partitions)
