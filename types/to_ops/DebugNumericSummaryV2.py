# DebugNumericSummaryV2Op

import tensorflow as tf

output_dtype = tf.float64
tensor_debug_mode = 3
tensor_id = 247
input = tf.constant(0, shape=[100,100], dtype=tf.float16)
tf.raw_ops.DebugNumericSummaryV2(input=input, output_dtype=output_dtype, tensor_debug_mode=tensor_debug_mode, tensor_id=tensor_id)
