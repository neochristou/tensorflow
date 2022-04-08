# StringFormatOp

import tensorflow as tf

template = "{}"
placeholder = "{}"
summarize = 3
inputs = tf.constant(0, shape=[10], dtype=tf.int32)
tf.raw_ops.StringFormat(inputs=inputs, template=template, placeholder=placeholder, summarize=summarize)
