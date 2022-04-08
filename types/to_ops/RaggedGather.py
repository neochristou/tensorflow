# RaggedGatherOp

import tensorflow as tf

OUTPUT_RAGGED_RANK = 1
params_nested_splits = tf.constant(0, shape=[7], dtype=tf.int64)
params_dense_values = tf.constant(1, shape=[12], dtype=tf.int32)
indices = tf.constant(0, shape=[6], dtype=tf.int64)
tf.raw_ops.RaggedGather(params_nested_splits=params_nested_splits, params_dense_values=params_dense_values, indices=indices, OUTPUT_RAGGED_RANK=OUTPUT_RAGGED_RANK)
