# 2022-01-31 11:00:22.401346: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/LSTMBlockCellGrad_e48c684f3d0ae82ecd655b946015cb60.py", line 19, in <module>    tf.raw_ops.LSTMBlockCellGrad(x=x, cs_prev=cs_prev, h_prev=h_prev, w=w, wci=wci, wcf=wcf, wco=wco, b=b, i=i, cs=cs, f=f, o=o, ci=ci, co=co, cs_grad=cs_grad, h_grad=h_grad)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: lstm_block_cell_grad() missing 1 required positional argument: 'use_peephole'

import tensorflow as tf

x = tf.constant(0.837607, shape=[28, 29], dtype=tf.float32)
cs_prev = tf.constant(-3.5e+35, shape=[13, 7], dtype=tf.float32)
h_prev = tf.constant(3.5e+35, shape=[13, 5, 2], dtype=tf.float32)
w = tf.constant(0, shape=[28, 17], dtype=tf.float32)
wci = tf.constant(1, shape=[28, 17], dtype=tf.float32)
wcf = tf.constant(0.837607, shape=[28, 29], dtype=tf.float32)
wco = tf.constant(0.592631638, shape=[28, 17], dtype=tf.float32)
b = tf.constant(0.592631638, shape=[28, 17], dtype=tf.float32)
i = tf.constant([], shape=[0], dtype=tf.float32)
cs = tf.constant(0.592631638, shape=[28, 17], dtype=tf.float32)
f = tf.constant(0.837607, shape=[28, 29], dtype=tf.float32)
o = tf.constant(0.837607, shape=[28, 29], dtype=tf.float32)
ci = tf.constant(0.837607, shape=[28, 29], dtype=tf.float32)
co = tf.constant(0.837607, shape=[28, 29], dtype=tf.float32)
cs_grad = tf.constant(0.837607, shape=[28, 29], dtype=tf.float32)
h_grad = tf.constant(0.837607, shape=[28, 29], dtype=tf.float32)
tf.raw_ops.LSTMBlockCellGrad(x=x, cs_prev=cs_prev, h_prev=h_prev, w=w, wci=wci, wcf=wcf, wco=wco,
                             b=b, i=i, cs=cs, f=f, o=o, ci=ci, co=co, cs_grad=cs_grad, h_grad=h_grad)
