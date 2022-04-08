# InvertPermutationOp

import tensorflow as tf

x = tf.constant([1,0], shape=[2], dtype=tf.int32)
tf.raw_ops.InvertPermutation(x=x)
