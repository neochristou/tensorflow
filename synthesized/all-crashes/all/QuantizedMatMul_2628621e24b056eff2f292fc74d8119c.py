# QuantizedMatMulOp

import tensorflow as tf

Toutput = tf.qint32
transpose_a = True
transpose_b = False
Tactivation = tf.quint8
a = tf.constant(11, shape=[3,4], dtype=tf.quint8)
b = tf.constant(11, shape=[3,4], dtype=tf.quint8)
min_a = tf.constant([], shape=[0], dtype=tf.float32)
max_a = tf.constant(-12, shape=[1], dtype=tf.float32)
min_b = tf.constant(-12, shape=[1], dtype=tf.float32)
max_b = tf.constant(-12, shape=[1], dtype=tf.float32)
tf.raw_ops.QuantizedMatMul(a=a, b=b, min_a=min_a, max_a=max_a, min_b=min_b, max_b=max_b, Toutput=Toutput, transpose_a=transpose_a, transpose_b=transpose_b, Tactivation=Tactivation)
