#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/WriteRawProtoSummary_8f5c4ed00269118593185ac23881e758.py", line 3    arg_0 = tf.constant(?, shape=[], dtype=tf.resource)                        ^SyntaxError: invalid syntax

import tensorflow as tf

arg_0 = tf.constant(?, shape=[], dtype=tf.resource)
arg_1 = tf.constant(1250999896764, shape=[], dtype=tf.int64)
arg_2 = tf.constant("\n\005\025\000\000(B", shape=[], dtype=tf.string)
tf.raw_ops.WriteRawProtoSummary(writer=arg_0, step=arg_1, tensor=arg_2)