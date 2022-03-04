import tensorflow as tf

t = tf.constant(0, shape=[3,5,4,2], dtype=tf.float32)
m = tf.constant([], shape=[0], dtype=tf.float32)
v = tf.constant(0.317702532, shape=[2], dtype=tf.float32)
beta = tf.constant(0.317702532, shape=[2], dtype=tf.float32)
gamma = tf.constant(0.317702532, shape=[2], dtype=tf.float32)
tf.raw_ops.BatchNormOp(t=t, m=m, v=v, beta=beta, gamma=gamma)