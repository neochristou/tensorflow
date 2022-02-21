import tensorflow as tf

x = tf.constant(0, shape=[17], dtype=tf.float32)
cs_prev = tf.constant(0.592631638, shape=[28,17], dtype=tf.float32)
h_prev = tf.constant(3.5e+35, shape=[22], dtype=tf.float32)
w = tf.constant(0, shape=[17], dtype=tf.float32)
wci = tf.constant(-3.5e+35, shape=[28,29], dtype=tf.float32)
wcf = tf.constant(-3.5e+35, shape=[28,17], dtype=tf.float32)
wco = tf.constant(0.592631638, shape=[28,17], dtype=tf.float32)
b = tf.constant(0.837607, shape=[28,29], dtype=tf.float32)
tf.raw_ops.LSTMBlockCell(x=x, cs_prev=cs_prev, h_prev=h_prev, w=w, wci=wci, wcf=wcf, wco=wco, b=b)