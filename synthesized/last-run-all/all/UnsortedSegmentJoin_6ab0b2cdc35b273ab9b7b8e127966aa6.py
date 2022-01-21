import tensorflow as tf

arg_0 = tf.constant("this", shape=[12], dtype=tf.string)
arg_1 = tf.constant(0, shape=[12], dtype=tf.int64)
arg_2 = tf.constant(0, shape=[12], dtype=tf.int64)
tf.raw_ops.UnsortedSegmentJoin(inputs=arg_0, segment_ids=arg_1, num_segments=arg_2)