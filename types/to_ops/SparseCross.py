# SparseCrossOp

import tensorflow as tf

hashed_output = True
num_buckets = 1000
hash_key = 956888297470
out_type = tf.int64
internal_type = DT_STRING
indices = tf.constant(0, shape=[3,2], dtype=tf.int64)
values = tf.constant(0, shape=[1,2], dtype=tf.int64)
shapes = tf.constant(0, shape=[2,2], dtype=tf.int64)
dense_inputs = tf.constant("-FC1", shape=[3], dtype=tf.string)
tf.raw_ops.SparseCross(indices=indices, values=values, shapes=shapes, dense_inputs=dense_inputs, hashed_output=hashed_output, num_buckets=num_buckets, hash_key=hash_key, out_type=out_type, internal_type=internal_type)
