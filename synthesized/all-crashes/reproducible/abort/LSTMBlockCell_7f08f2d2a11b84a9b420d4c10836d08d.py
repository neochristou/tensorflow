# Signal -6;2022-03-07 19:06:37.022350: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory2022-03-07 19:06:37.022400: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.2022-03-07 19:06:37.922498: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory2022-03-07 19:06:37.922556: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)2022-03-07 19:06:37.922579: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (devel): /proc/driver/nvidia/version does not exist2022-03-07 19:06:37.922845: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-07 19:06:37.927233: F tensorflow/core/framework/tensor_shape.cc:45] Check failed: NDIMS == dims() (1 vs. 2)Asking for tensor of 1 dimensions from a tensor of 2 dimensions

# LSTMBlockCellOp

import tensorflow as tf

forget_bias = 1
cell_clip = 0
use_peephole = False
x = tf.constant(0.837607, shape=[28,29], dtype=tf.float32)
cs_prev = tf.constant(0, shape=[28,17], dtype=tf.float32)
h_prev = tf.constant(0.592631638, shape=[28,17], dtype=tf.float32)
w = tf.constant(0.887386262, shape=[46,68], dtype=tf.float32)
wci = tf.constant(0, shape=[], dtype=tf.float32)
wcf = tf.constant(0, shape=[17], dtype=tf.float32)
wco = tf.constant(0.592631638, shape=[28,17], dtype=tf.float32)
b = tf.constant(0.75259006, shape=[68], dtype=tf.float32)
tf.raw_ops.LSTMBlockCell(x=x, cs_prev=cs_prev, h_prev=h_prev, w=w, wci=wci, wcf=wcf, wco=wco, b=b, forget_bias=forget_bias, cell_clip=cell_clip, use_peephole=use_peephole)