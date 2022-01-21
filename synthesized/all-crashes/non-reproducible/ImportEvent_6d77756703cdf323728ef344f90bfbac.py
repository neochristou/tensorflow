#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/ImportEvent_6d77756703cdf323728ef344f90bfbac.py", line 3    arg_0 = tf.constant(?, shape=[], dtype=tf.resource)                        ^SyntaxError: invalid syntax

import tensorflow as tf

arg_0 = tf.constant(?, shape=[], dtype=tf.resource)
arg_1 = tf.constant("[]", shape=[], dtype=tf.string)
tf.raw_ops.ImportEvent(writer=arg_0, event=arg_1)