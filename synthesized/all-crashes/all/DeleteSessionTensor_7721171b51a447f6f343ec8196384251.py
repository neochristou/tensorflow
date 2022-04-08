# DeleteSessionTensorOp

import tensorflow as tf

handle = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.DeleteSessionTensor(handle=handle)
