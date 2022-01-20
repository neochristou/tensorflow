#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/MirrorPad_5a4f1b089094603b1766ebbcedcbe6c1.py", line 3    arg_0 = tf.constant(?, shape=[2,5], dtype=tf.complex64)                        ^SyntaxError: invalid syntax

import tensorflow as tf

arg_0 = tf.constant(?, shape=[2,5], dtype=tf.complex64)
arg_1 = tf.constant(1879048192, shape=[], dtype=tf.int32)
tf.raw_ops.MirrorPad(input=arg_0, paddings=arg_1)