import tensorflow as tf

OUTPUT_RAGGED_RANK = 2
params_nested_splits = tf.constant(0, shape=[5], dtype=tf.int64)
params_dense_values = tf.constant(1879048192, shape=[], dtype=tf.int64)
indices = tf.constant(-1879048192, shape=[7], dtype=tf.int32)
name = tf.constant(-8608480567731124087, shape=[], dtype=tf.int64)
tf.raw_ops.RaggedGather(params_nested_splits=params_nested_splits, params_dense_values=params_dense_values, indices=indices, OUTPUT_RAGGED_RANK=OUTPUT_RAGGED_RANK, name=name)