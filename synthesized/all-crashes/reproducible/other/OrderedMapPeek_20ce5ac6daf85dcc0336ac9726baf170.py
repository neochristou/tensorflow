# Signal --4;2022-03-07 19:07:09.758885: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory2022-03-07 19:07:09.758934: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.2022-03-07 19:07:10.836386: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory2022-03-07 19:07:10.836438: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)2022-03-07 19:07:10.836464: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (devel): /proc/driver/nvidia/version does not exist2022-03-07 19:07:10.836729: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

# MapPeekOp

import tensorflow as tf

dtypes = [tf.float32, tf.float32]
capacity = 0
memory_limit = 0
container = ""
shared_name = "MapStagingArea"
key = tf.constant(-1879048192, shape=[], dtype=tf.int64)
indices = tf.constant([0,2], shape=[2], dtype=tf.int32)
tf.raw_ops.OrderedMapPeek(key=key, indices=indices, dtypes=dtypes, capacity=capacity, memory_limit=memory_limit, container=container, shared_name=shared_name)