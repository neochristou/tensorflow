import tensorflow as tf

arg_0 = tf.constant(0, shape=[], dtype=tf.int64)
arg_1 = tf.constant(1, shape=[3], dtype=tf.int32)
tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=arg_0, rt_dense_values=arg_1)