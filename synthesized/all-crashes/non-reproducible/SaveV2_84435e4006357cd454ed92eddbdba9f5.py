#   File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/SaveV2_84435e4006357cd454ed92eddbdba9f5.py", line 8    tensors = tf.constant(?, shape=[2,2], dtype=tf.complex128)                          ^SyntaxError: invalid syntax

# SaveV2

import tensorflow as tf

prefix = tf.constant("-00000", shape=[], dtype=tf.string)
tensor_names = tf.constant("[]", shape=[2], dtype=tf.string)
shape_and_slices = tf.constant("[]", shape=[2], dtype=tf.string)
tensors = tf.constant(?, shape=[2,2], dtype=tf.complex128)
tf.raw_ops.SaveV2(prefix=prefix, tensor_names=tensor_names, shape_and_slices=shape_and_slices, tensors=tensors)