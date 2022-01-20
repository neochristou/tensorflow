# Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/CSRSparseMatrixComponents_278e10e6e344e5d87104a6e01a0a3aab.py", line 3, in <module>    arg_0 = tf.constant(Variant<type, shape=[], dtype=tf.variant)NameError: name 'Variant' is not defined

import tensorflow as tf

arg_0 = tf.constant(Variant<type, shape=[], dtype=tf.variant)
arg_1 = tf.constant(0, shape=[], dtype=tf.int32)
tf.raw_ops.CSRSparseMatrixComponents(csr_sparse_matrix=arg_0, index=arg_1)