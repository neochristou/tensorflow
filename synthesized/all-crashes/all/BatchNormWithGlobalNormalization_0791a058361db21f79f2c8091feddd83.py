# BatchNormOp

import tensorflow as tf

variance_epsilon = 0.001
scale_after_normalization = True
t = tf.constant(0, shape=[3,5,4,2], dtype=tf.float32)
m = tf.constant([], shape=[0], dtype=tf.float32)
v = tf.constant([0.317702532,0.948696], shape=[2], dtype=tf.float32)
beta = tf.constant([0.317702532,0.948696], shape=[2], dtype=tf.float32)
gamma = tf.constant([0.317702532,0.948696], shape=[2], dtype=tf.float32)
tf.raw_ops.BatchNormWithGlobalNormalization(t=t, m=m, v=v, beta=beta, gamma=gamma, variance_epsilon=variance_epsilon, scale_after_normalization=scale_after_normalization)