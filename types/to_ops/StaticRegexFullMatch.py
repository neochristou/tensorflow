# StaticRegexFullMatchOp

import tensorflow as tf

pattern = "^s3://.*"
input = tf.constant("/tmp/extension_type_teste8qs34a3mb8f30j4/variables/variables", shape=[], dtype=tf.string)
tf.raw_ops.StaticRegexFullMatch(input=input, pattern=pattern)
