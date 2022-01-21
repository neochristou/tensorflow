#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/CreateSummaryFileWriter_7174f2d87bf6c401f42953ac027e7656.py", line 3    arg_0 = tf.constant(?, shape=[], dtype=tf.resource)                        ^SyntaxError: invalid syntax

import tensorflow as tf

arg_0 = tf.constant(?, shape=[], dtype=tf.resource)
arg_1 = tf.constant("[]", shape=[0], dtype=tf.string)
arg_2 = tf.constant(10, shape=[], dtype=tf.int32)
arg_3 = tf.constant(10, shape=[], dtype=tf.int32)
arg_4 = tf.constant("/tmp/callbacks_v1_testvyt7jziu/tmp_ddyqpoe/train", shape=[], dtype=tf.string)
tf.raw_ops.CreateSummaryFileWriter(writer=arg_0, logdir=arg_1, max_queue=arg_2, flush_millis=arg_3, filename_suffix=arg_4)