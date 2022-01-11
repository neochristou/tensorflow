import tensorflow as tf

arg_0 = tf.constant(0, shape=[2,3], dtype=tf.float32)
arg_1 = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
arg_2 = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
arg_3 = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
tf.raw_ops.FakeQuantWithMinMaxVarsGradient(gradients=arg_0, inputs=arg_1, min=arg_2, max=arg_3)