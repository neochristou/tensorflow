# UnsortedSegmentJoinOp

import tensorflow as tf

separator = ""
inputs = tf.constant("this", shape=[4], dtype=tf.string)
segment_ids = tf.constant(0, shape=[4], dtype=tf.int32)
num_segments = tf.constant(1, shape=[], dtype=tf.int32)
tf.raw_ops.UnsortedSegmentJoin(inputs=inputs, segment_ids=segment_ids, num_segments=num_segments, separator=separator)
