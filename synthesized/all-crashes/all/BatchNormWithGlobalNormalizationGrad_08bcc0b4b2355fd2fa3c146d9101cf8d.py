# BatchNormGradOp

import tensorflow as tf

variance_epsilon = 0.001
scale_after_normalization = True
t = tf.constant(-1.5e+300, shape=[5,13,5,2], dtype=tf.float64)
m = tf.constant(0.81185869772053976, shape=[5], dtype=tf.float64)
v = tf.constant(0.81185869772053976, shape=[5], dtype=tf.float64)
gamma = tf.constant(0.81185869772053976, shape=[5], dtype=tf.float64)
backprop = tf.constant(0.417022004702574, shape=[3,5,4,5], dtype=tf.float64)
tf.raw_ops.BatchNormWithGlobalNormalizationGrad(t=t, m=m, v=v, gamma=gamma, backprop=backprop, variance_epsilon=variance_epsilon, scale_after_normalization=scale_after_normalization)
