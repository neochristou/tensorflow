# RaggedCrossOp

import tensorflow as tf

input_order = "R"
hashed_output = False
num_buckets = 0
hash_key = 956888297470
out_values_type = DT_STRING
out_row_splits_type = DT_INT64
ragged_values = tf.constant("a", shape=[3], dtype=tf.string)
ragged_row_splits = tf.constant(0, shape=[4], dtype=tf.int64)
tf.raw_ops.RaggedCross(ragged_values=ragged_values, ragged_row_splits=ragged_row_splits, sparse_indices=sparse_indices, sparse_values=sparse_values, sparse_shape=sparse_shape, dense_inputs=dense_inputs, input_order=input_order, hashed_output=hashed_output)
