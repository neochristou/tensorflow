# StringStripOp

import tensorflow as tf

input = tf.constant("[pigs,on,the,wing,animals]", shape=[2], dtype=tf.string)
tf.raw_ops.StringStrip(input=input)
