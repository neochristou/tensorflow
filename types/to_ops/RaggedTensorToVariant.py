# RaggedTensorToVariantOp

import tensorflow as tf

batched_input = True
rt_nested_splits = tf.constant(0, shape=[3], dtype=tf.int64)
rt_dense_values = tf.constant(1, shape=[3], dtype=tf.int32)
tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, batched_input=batched_input)
