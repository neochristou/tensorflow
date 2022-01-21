#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/SparseReshape_e4e80f0dbeedfca9a9822fbb2922e960.py", line 3    arg_0 = tf.constant(012, shape=[14,1], dtype=tf.int64)                          ^SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

import tensorflow as tf

arg_0 = tf.constant(012, shape=[14,1], dtype=tf.int64)
arg_1 = tf.constant(-1879048192, shape=[1], dtype=tf.int64)
arg_2 = tf.constant(15, shape=[1], dtype=tf.int64)
tf.raw_ops.SparseReshape(input_indices=arg_0, input_shape=arg_1, new_shape=arg_2)