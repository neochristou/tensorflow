import tensorflow as tf

tag = tf.constant("foo", shape=[], dtype=tf.string)
tensor = tf.constant(1, shape=[], dtype=tf.bool)
serialized_summary_metadata = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.SummaryTensorOpV2(tag=tag, tensor=tensor, serialized_summary_metadata=serialized_summary_metadata)