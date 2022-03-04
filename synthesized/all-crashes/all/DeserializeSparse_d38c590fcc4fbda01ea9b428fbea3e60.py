import tensorflow as tf

serialized_sparse = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.DeserializeSparse(serialized_sparse=serialized_sparse)