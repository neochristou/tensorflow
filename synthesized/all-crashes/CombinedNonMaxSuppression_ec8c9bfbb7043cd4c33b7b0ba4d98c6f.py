import tensorflow as tf

arg_0 = tf.constant(0, shape=[1,1,6,4], dtype=tf.float32)
arg_1 = tf.constant(0.9, shape=[1,1,6], dtype=tf.float32)
arg_2 = tf.constant(65534, shape=[], dtype=tf.int32)
arg_3 = tf.constant(1879048192, shape=[], dtype=tf.int32)
arg_4 = tf.constant(0, shape=[], dtype=tf.float32)
arg_5 = tf.constant(0.5, shape=[], dtype=tf.float32)
tf.raw_ops.CombinedNonMaxSuppression(boxes=arg_0, scores=arg_1, max_output_size_per_class=arg_2, max_total_size=arg_3, iou_threshold=arg_4, score_threshold=arg_5)