# ListDiffOp

import tensorflow as tf

out_idx = DT_INT32
x = tf.constant([0,1], shape=[2], dtype=tf.int32)
y = tf.constant([1,0], shape=[2], dtype=tf.int32)
tf.raw_ops.ListDiff(x=x, y=y, out_idx=out_idx)
