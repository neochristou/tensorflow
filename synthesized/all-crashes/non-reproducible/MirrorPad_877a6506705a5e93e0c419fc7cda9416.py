#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/MirrorPad_877a6506705a5e93e0c419fc7cda9416.py", line 3    arg_0 = tf.constant(?, shape=[2,5], dtype=tf.complex64)                        ^SyntaxError: invalid syntax

import tensorflow as tf

arg_0 = tf.constant(?, shape=[2,5], dtype=tf.complex64)
arg_1 = tf.constant(0, shape=[2,2], dtype=tf.int32)
tf.raw_ops.MirrorPad(input=arg_0, paddings=arg_1)