import tensorflow as tf

arg_0 = tf.constant("/tmp/warm_starting_util_testwqbi12f2/tmp824v67i0/model-0", shape=[], dtype=tf.string)
arg_1 = tf.constant("/tmp/warm_starting_util_testwqbi12f2/tmp824v67i0/model-0", shape=[], dtype=tf.string)
arg_2 = tf.constant(0, shape=[], dtype=tf.int64)
arg_3 = tf.constant(0, shape=[3], dtype=tf.int64)
arg_4 = tf.constant(.420, shape=[4,1], dtype=tf.float32)
tf.raw_ops.LoadAndRemapMatrix(ckpt_path=arg_0, old_tensor_name=arg_1, row_remapping=arg_2, col_remapping=arg_3, initializing_values=arg_4)