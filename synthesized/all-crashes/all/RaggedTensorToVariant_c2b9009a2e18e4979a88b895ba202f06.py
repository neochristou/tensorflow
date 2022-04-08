# RaggedTensorToVariantOp

import tensorflow as tf

batched_input = False
rt_nested_splits = tf.constant(0, shape=[], dtype=tf.int64)
rt_dense_values = tf.constant(203, shape=[3], dtype=tf.int32)
tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, batched_input=batched_input)
