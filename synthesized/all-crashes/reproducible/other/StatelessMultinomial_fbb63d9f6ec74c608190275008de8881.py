# Signal --4;2022-02-15 18:04:28.578667: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-02-15 18:04:28.583253: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 15032385536 exceeds 10% of free system memory.

import tensorflow as tf

logits = tf.constant(-1.20397282, shape=[1,2], dtype=tf.float32)
num_samples = tf.constant(1879048192, shape=[], dtype=tf.int32)
seed = tf.constant(1987023866, shape=[2], dtype=tf.int64)
tf.raw_ops.StatelessMultinomial(logits=logits, num_samples=num_samples, seed=seed)