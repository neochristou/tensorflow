# EnterOp

import tensorflow as tf

frame_name = "while"
is_constant = False
parallel_iterations = 10
data = tf.constant(0, shape=[3], dtype=tf.int32)
tf.raw_ops.RefEnter(data=data, frame_name=frame_name, is_constant=is_constant, parallel_iterations=parallel_iterations)
