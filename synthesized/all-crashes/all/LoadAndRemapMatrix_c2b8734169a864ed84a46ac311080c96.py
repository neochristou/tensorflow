import tensorflow as tf

ckpt_path = tf.constant("/tmp/warm_starting_util_testbdiyt3ov/tmp0qqyxz7g/model-0", shape=[], dtype=tf.string)
old_tensor_name = tf.constant("/tmp/warm_starting_util_testbdiyt3ov/tmp0qqyxz7g/model-0", shape=[], dtype=tf.string)
row_remapping = tf.constant(0, shape=[], dtype=tf.int64)
col_remapping = tf.constant(3, shape=[3], dtype=tf.int64)
initializing_values = tf.constant([], shape=[0,1], dtype=tf.float32)
tf.raw_ops.LoadAndRemapMatrixOp(ckpt_path=ckpt_path, old_tensor_name=old_tensor_name, row_remapping=row_remapping, col_remapping=col_remapping, initializing_values=initializing_values)