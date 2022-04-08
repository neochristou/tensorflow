# MatrixDiagOp

import tensorflow as tf

diagonal = tf.constant(1, shape=[4], dtype=tf.float32)
tf.raw_ops.BatchMatrixDiag(diagonal=diagonal)
