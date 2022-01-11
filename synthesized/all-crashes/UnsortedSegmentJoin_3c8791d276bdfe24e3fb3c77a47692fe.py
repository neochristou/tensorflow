import tensorflow as tf

arg_0 = tf.constant("this", shape=[4], dtype=tf.string)
arg_1 = tf.constant(1, shape=[], dtype=tf.int32)
arg_2 = tf.constant(0, shape=[4], dtype=tf.int32)
tf.raw_ops.UnsortedSegmentJoin(inputs=arg_0, segment_ids=arg_1, num_segments=arg_2)