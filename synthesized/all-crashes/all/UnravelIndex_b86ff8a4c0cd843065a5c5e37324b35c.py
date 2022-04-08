# UnravelIndexOp

import tensorflow as tf

indices = tf.constant(-536870912, shape=[3], dtype=tf.int32)
dims = tf.constant(-536870912, shape=[3], dtype=tf.int32)
tf.raw_ops.UnravelIndex(indices=indices, dims=dims)
