import tensorflow as tf

y_backprop = tf.constant(-3.5e+35, shape=[3,2,4,2], dtype=tf.float32)
x = tf.constant(-0.196384236, shape=[3,2,4,2], dtype=tf.float32)
scale = tf.constant([], shape=[0], dtype=tf.float32)
reserve_space_1 = tf.constant(1, shape=[2], dtype=tf.float32)
reserve_space_2 = tf.constant(1, shape=[2], dtype=tf.float32)
reserve_space_3 = tf.constant(-0.196384236, shape=[3,2,4,2], dtype=tf.float32)
tf.raw_ops.FusedBatchNormGradOpV3(y_backprop=y_backprop, x=x, scale=scale, reserve_space_1=reserve_space_1, reserve_space_2=reserve_space_2, reserve_space_3=reserve_space_3)