# DeserializeSparseOp

import tensorflow as tf

dtype = tf.int32
serialized_sparse = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.DeserializeManySparse(serialized_sparse=serialized_sparse, dtype=dtype)
