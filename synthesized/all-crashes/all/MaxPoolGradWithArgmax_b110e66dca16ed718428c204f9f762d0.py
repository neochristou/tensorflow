import tensorflow as tf

input = tf.constant(111213, shape=[2,2,2,1], dtype=tf.float32)
grad = tf.constant(111, shape=[2,3,3,1], dtype=tf.float32)
argmax = tf.constant(013, shape=[2,2,2,1], dtype=tf.int64)
tf.raw_ops.MaxPoolingGradWithArgmaxOp(input=input, grad=grad, argmax=argmax)