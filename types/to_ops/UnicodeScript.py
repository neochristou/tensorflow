# UnicodeScriptOp

import tensorflow as tf

input = tf.constant([-100,16777215], shape=[2], dtype=tf.int32)
tf.raw_ops.UnicodeScript(input=input)
