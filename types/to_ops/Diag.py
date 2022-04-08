# DiagOp

import tensorflow as tf

diagonal = tf.constant(0.545883179, shape=[3], dtype=tf.float32)
tf.raw_ops.Diag(diagonal=diagonal)
