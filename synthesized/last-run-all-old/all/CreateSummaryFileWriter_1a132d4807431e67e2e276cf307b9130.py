import tensorflow as tf

writer = tf.constant("/tmp/callbacks_test4bzt8bmj/tmpsn9x861m/train", shape=[], dtype=tf.string)
logdir = tf.constant(-536870912, shape=[], dtype=tf.int32)
max_queue = tf.constant([], shape=[0], dtype=tf.int32)
flush_millis = tf.constant("/tmp/callbacks_test4bzt8bmj/tmpsn9x861m/train", shape=[], dtype=tf.string)
tf.raw_ops.CreateSummaryFileWriter(writer=writer, logdir=logdir, max_queue=max_queue, flush_millis=flush_millis)