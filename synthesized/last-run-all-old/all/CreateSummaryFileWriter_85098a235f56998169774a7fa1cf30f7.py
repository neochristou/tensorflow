import tensorflow as tf

writer = tf.constant("/tmp/sidecar_evaluator_testzmdf_is7/tmpid3l7ylo/summary/train", shape=[], dtype=tf.string)
logdir = tf.constant(10, shape=[], dtype=tf.int32)
max_queue = tf.constant([], shape=[0], dtype=tf.int32)
flush_millis = tf.constant("/tmp/sidecar_evaluator_testzmdf_is7/tmpid3l7ylo/summary/train", shape=[], dtype=tf.string)
tf.raw_ops.CreateSummaryFileWriter(writer=writer, logdir=logdir, max_queue=max_queue, flush_millis=flush_millis)