import tensorflow as tf

arg_0 = tf.constant("/tmp/sidecar_evaluator_testzmdf_is7/tmpid3l7ylo/summary/train", shape=[], dtype=tf.string)
arg_1 = tf.constant(10, shape=[], dtype=tf.int32)
arg_2 = tf.constant([], shape=[0], dtype=tf.int32)
arg_3 = tf.constant("/tmp/sidecar_evaluator_testzmdf_is7/tmpid3l7ylo/summary/train", shape=[], dtype=tf.string)
tf.raw_ops.CreateSummaryFileWriter(writer=arg_0, logdir=arg_1, max_queue=arg_2, flush_millis=arg_3)