# StaticRegexReplaceOp

import tensorflow as tf

pattern = ""
rewrite = "x"
replace_global = True
input = tf.constant("[abc,1]", shape=[2], dtype=tf.string)
tf.raw_ops.StaticRegexReplace(input=input, pattern=pattern, rewrite=rewrite, replace_global=replace_global)
