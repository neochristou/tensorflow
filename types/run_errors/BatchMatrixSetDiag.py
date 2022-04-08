# MatrixSetDiagOp

import tensorflow as tf

input = tf.constant(-0.00396825466, shape=[2,3,3], dtype=tf.float32)
diagonal = tf.constant(0.0198412724, shape=[2,3], dtype=tf.float32)
tf.raw_ops.BatchMatrixSetDiag(input=input, diagonal=diagonal)
