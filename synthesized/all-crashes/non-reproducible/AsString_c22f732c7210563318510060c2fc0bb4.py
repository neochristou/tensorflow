# 2022-03-07 19:05:56.353447: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory2022-03-07 19:05:56.353489: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.2022-03-07 19:06:03.744087: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory2022-03-07 19:06:03.744132: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)2022-03-07 19:06:03.744153: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (devel): /proc/driver/nvidia/version does not exist2022-03-07 19:06:03.744523: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# AsStringOp

import tensorflow as tf

precision = -1
scientific = False
shortest = False
width = -1
fill = ""
input = tf.constant(False, shape=[], dtype=tf.bool)
tf.raw_ops.AsString(input=input, precision=precision, scientific=scientific, shortest=shortest, width=width, fill=fill)