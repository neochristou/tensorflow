import tensorflow as tf

arg_0 = tf.constant(1.5e+300, shape=[12,10,19], dtype=tf.float64)
arg_1 = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.DynamicPartition(data=arg_0, partitions=arg_1)