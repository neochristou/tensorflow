# RestoreOp

import tensorflow as tf

dt = tf.bool
preferred_shard = -1
file_pattern = tf.constant("/home/neo/.cache/bazel/_bazel_neo/393d995a358fc7b156deb55ee2581794/execroot/org_tensorflow/_tmp/aa8a8c78961330944213844b04568343/tensor_simple", shape=[], dtype=tf.string)
tensor_name = tf.constant("tensor_bool", shape=[], dtype=tf.string)
tf.raw_ops.Restore(file_pattern=file_pattern, tensor_name=tensor_name, dt=dt, preferred_shard=preferred_shard)
