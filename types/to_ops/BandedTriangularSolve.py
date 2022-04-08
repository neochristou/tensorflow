# BandedTriangularSolveOpCpu

import tensorflow as tf

lower = True
adjoint = False
matrix = tf.constant(1, shape=[3,3], dtype=tf.float32)
rhs = tf.constant(1, shape=[3,3], dtype=tf.float32)
tf.raw_ops.BandedTriangularSolve(matrix=matrix, rhs=rhs, lower=lower, adjoint=adjoint)
