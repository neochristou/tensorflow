# MergeV2Checkpoints

import tensorflow as tf

delete_old_dirs = True
checkpoint_prefixes = tf.constant("-00000", shape=[1], dtype=tf.string)
destination_prefix = tf.constant("/tmp/extension_type_teste8qs34a3mb8f30j4/variables/variables", shape=[], dtype=tf.string)
tf.raw_ops.MergeV2Checkpoints(checkpoint_prefixes=checkpoint_prefixes, destination_prefix=destination_prefix, delete_old_dirs=delete_old_dirs)
