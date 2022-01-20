import tensorflow as tf

arg_0 = tf.constant(-3.5, shape=[1], dtype=tf.float32)
arg_1 = tf.constant(-3.5, shape=[1], dtype=tf.float32)
arg_2 = tf.constant(-3.5, shape=[1], dtype=tf.float32)
arg_3 = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.QuantizeAndDequantizeV3(input=arg_0, input_min=arg_1, input_max=arg_2, num_bits=arg_3)