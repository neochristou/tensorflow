import tensorflow as tf

arg_0 = tf.constant("/tmp/warm_starting_util_test4qlrae3v/tmp7t4euxnl/model-0", shape=[], dtype=tf.string)
arg_1 = tf.constant("/tmp/warm_starting_util_test4qlrae3v/tmp7t4euxnl/model-0", shape=[], dtype=tf.string)
arg_2 = tf.constant(0, shape=[], dtype=tf.int64)
arg_3 = tf.constant(3, shape=[3], dtype=tf.int64)
arg_4 = tf.constant([], shape=[0,1], dtype=tf.float32)
tf.raw_ops.LoadAndRemapMatrix(ckpt_path=arg_0, old_tensor_name=arg_1, row_remapping=arg_2, col_remapping=arg_3, initializing_values=arg_4)