#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/WriteSummary_6e282a7faafc617317d9a4707b5c1ebc.py", line 3    arg_0 = tf.constant(?, shape=[], dtype=tf.resource)                        ^SyntaxError: invalid syntax

import tensorflow as tf

arg_0 = tf.constant(?, shape=[], dtype=tf.resource)
arg_1 = tf.constant(-1879048192, shape=[], dtype=tf.int64)
arg_2 = tf.constant(42, shape=[], dtype=tf.int32)
arg_3 = tf.constant("tag", shape=[], dtype=tf.string)
arg_4 = tf.constant("tag", shape=[], dtype=tf.string)
tf.raw_ops.WriteSummary(writer=arg_0, step=arg_1, tensor=arg_2, tag=arg_3, summary_metadata=arg_4)