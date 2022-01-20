#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/CreateSummaryFileWriter_b7e58e571fb0a91c3072b13997c005f6.py", line 3    arg_0 = tf.constant(?, shape=[], dtype=tf.resource)                        ^SyntaxError: invalid syntax

import tensorflow as tf

arg_0 = tf.constant(?, shape=[], dtype=tf.resource)
arg_1 = tf.constant(".22416", shape=[], dtype=tf.string)
arg_2 = tf.constant(10, shape=[], dtype=tf.int32)
arg_3 = tf.constant(10, shape=[], dtype=tf.int32)
arg_4 = tf.constant("/tmp/base_layer_test5hpx1lft/tmp0j7pti1q", shape=[], dtype=tf.string)
tf.raw_ops.CreateSummaryFileWriter(writer=arg_0, logdir=arg_1, max_queue=arg_2, flush_millis=arg_3, filename_suffix=arg_4)