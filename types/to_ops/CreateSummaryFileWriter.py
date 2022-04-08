# CreateSummaryFileWriterOp

import tensorflow as tf

writer = tf.constant("/tmp/summary_ops_test6sqdu4bq/tmphgkk_w0x", shape=[], dtype=tf.string)
logdir = tf.constant(10, shape=[], dtype=tf.int32)
max_queue = tf.constant(120000, shape=[], dtype=tf.int32)
flush_millis = tf.constant(".v2", shape=[], dtype=tf.string)
tf.raw_ops.CreateSummaryFileWriter(writer=writer, logdir=logdir, max_queue=max_queue, flush_millis=flush_millis)
