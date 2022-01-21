import tensorflow as tf

arg_0 = tf.constant("/tmp/callbacks_test4bzt8bmj/tmpsn9x861m/train", shape=[], dtype=tf.string)
arg_1 = tf.constant(-536870912, shape=[], dtype=tf.int32)
arg_2 = tf.constant([], shape=[0], dtype=tf.int32)
arg_3 = tf.constant("/tmp/callbacks_test4bzt8bmj/tmpsn9x861m/train", shape=[], dtype=tf.string)
tf.raw_ops.CreateSummaryFileWriter(writer=arg_0, logdir=arg_1, max_queue=arg_2, flush_millis=arg_3)