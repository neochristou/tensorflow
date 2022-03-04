import tensorflow as tf

rt_nested_splits = tf.constant(-8608480567731124087, shape=[], dtype=tf.int64)
rt_dense_values = tf.constant(0, shape=[7], dtype=tf.int64)
tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values)