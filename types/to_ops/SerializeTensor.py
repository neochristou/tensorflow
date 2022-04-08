# SerializeTensorOp

import tensorflow as tf

tensor = tf.constant(0, shape=[10], dtype=tf.float16)
tf.raw_ops.SerializeTensor(tensor=tensor)
