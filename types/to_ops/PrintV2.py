# PrintV2Op

import tensorflow as tf

output_stream = "log(error)"
end = "\n"
input = tf.constant("0", shape=[], dtype=tf.string)
tf.raw_ops.PrintV2(input=input, output_stream=output_stream, end=end)
