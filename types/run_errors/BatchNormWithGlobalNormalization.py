# BatchNormOp

import tensorflow as tf

variance_epsilon = 1e-05
scale_after_normalization = False
t = tf.constant(14.7, shape=[1,1,6,2], dtype=tf.float32)
m = tf.constant([10,20], shape=[2], dtype=tf.float32)
v = tf.constant([0.25,0.5], shape=[2], dtype=tf.float32)
beta = tf.constant([0.1,0.6], shape=[2], dtype=tf.float32)
gamma = tf.constant([1,2], shape=[2], dtype=tf.float32)
tf.raw_ops.BatchNormWithGlobalNormalization(t=t, m=m, v=v, beta=beta, gamma=gamma, variance_epsilon=variance_epsilon, scale_after_normalization=scale_after_normalization)
