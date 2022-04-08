# RestoreV2

import tensorflow as tf

dtypes = [tf.float32, tf.float32]
prefix = tf.constant("/tmp/convert_to_constants_testn8zapoj2/tmpm18tgdnj/frozen_saved_model/variables/variables", shape=[], dtype=tf.string)
tensor_names = tf.constant("[Variable,Variable_1]", shape=[2], dtype=tf.string)
shape_and_slices = tf.constant("[]", shape=[2], dtype=tf.string)
tf.raw_ops.RestoreV2(prefix=prefix, tensor_names=tensor_names, shape_and_slices=shape_and_slices, dtypes=dtypes)
