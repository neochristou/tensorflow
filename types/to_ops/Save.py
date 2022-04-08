# SaveOp

import tensorflow as tf

filename = tf.constant("/home/neo/.cache/bazel/_bazel_neo/393d995a358fc7b156deb55ee2581794/execroot/org_tensorflow/_tmp/96f47f6efe19215720e06210a454ddf5/tensor_simple-/Save", shape=[], dtype=tf.string)
tensor_names = tf.constant("tensor_bool", shape=[12], dtype=tf.string)
data = tf.constant(True, shape=[2], dtype=tf.bool)
tf.raw_ops.Save(filename=filename, tensor_names=tensor_names, data=data)
