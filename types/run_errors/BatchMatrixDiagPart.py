# MatrixDiagPartOp

import tensorflow as tf

input = tf.constant(0.0198567417, shape=[2,3,3], dtype=tf.float32)
tf.raw_ops.BatchMatrixDiagPart(input=input)
