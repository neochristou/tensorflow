# Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/RestoreSlice_9e309b7df1f14baec2a760be32c00230.py", line 5, in <module>    dt = DT_INT32NameError: name 'DT_INT32' is not defined

# RestoreSliceOp

import tensorflow as tf

dt = tf.int32
preferred_shard = -1
file_pattern = tf.constant(
    "/home/neo/.cache/bazel/_bazel_neo/393d995a358fc7b156deb55ee2581794/execroot/org_tensorflow/_tmp/a326e35e66efa0a2140c608a45463a71/tensor_int", shape=[], dtype=tf.string)
tensor_name = tf.constant("tensor_int", shape=[], dtype=tf.string)
shape_and_slice = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.RestoreSlice(file_pattern=file_pattern, tensor_name=tensor_name,
                        shape_and_slice=shape_and_slice, dt=dt, preferred_shard=preferred_shard)
