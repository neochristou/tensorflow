# SaveV2

import tensorflow as tf

prefix = tf.constant("-00000", shape=[], dtype=tf.string)
tensor_names = tf.constant("_CHECKPOINTABLE_OBJECT_GRAPH", shape=[1], dtype=tf.string)
shape_and_slices = tf.constant("[]", shape=[1], dtype=tf.string)
tensors = tf.constant("\n\020\n\016\010\001\022\nsignatures\n\000", shape=[], dtype=tf.string)
tf.raw_ops.SaveV2(prefix=prefix, tensor_names=tensor_names, shape_and_slices=shape_and_slices, tensors=tensors)
