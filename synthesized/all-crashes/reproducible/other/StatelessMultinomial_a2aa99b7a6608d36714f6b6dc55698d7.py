# Signal --4;2022-03-07 19:10:08.019810: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory2022-03-07 19:10:08.019864: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.2022-03-07 19:10:08.924968: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory2022-03-07 19:10:08.925025: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)2022-03-07 19:10:08.925049: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (devel): /proc/driver/nvidia/version does not exist2022-03-07 19:10:08.925340: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-03-07 19:10:08.929245: W tensorflow/core/framework/cpu_allocator_impl.cc:82] Allocation of 15032385536 exceeds 10% of free system memory.

# StatelessMultinomialOp

import tensorflow as tf

output_dtype = tf.int64
logits = tf.constant(-3.5e+35, shape=[1,2], dtype=tf.float32)
num_samples = tf.constant(1879048192, shape=[], dtype=tf.int32)
seed = tf.constant([1992996002,2535852961], shape=[2], dtype=tf.int64)
tf.raw_ops.StatelessMultinomial(logits=logits, num_samples=num_samples, seed=seed, output_dtype=output_dtype)