# GetSessionTensorOp

import tensorflow as tf

dtype = tf.float32
handle = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.GetSessionTensor(handle=handle, dtype=dtype)
