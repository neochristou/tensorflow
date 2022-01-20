import tensorflow as tf

arg_0 = tf.constant("/home/neo/.cache/bazel/_bazel_neo/098616a281617113c3854db5f68bcd26/execroot/org_tensorflow/_tmp/a326e35e66efa0a2140c608a45463a71/tensor_int", shape=[], dtype=tf.string)
arg_1 = tf.constant("tensor_int", shape=[], dtype=tf.string)
arg_2 = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.RestoreSlice(file_pattern=arg_0, tensor_name=arg_1, shape_and_slice=arg_2)