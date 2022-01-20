import tensorflow as tf

arg_0 = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.DeleteSessionTensor(handle=arg_0)