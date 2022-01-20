# Signal -6;2022-01-20 07:04:41.044480: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:04:41.046652: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-20 07:04:41.063752: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 0)Must have a one element tensor

import tensorflow as tf

arg_0 = tf.constant(0, shape=[], dtype=tf.float32)
arg_1 = tf.constant(-3.5, shape=[1], dtype=tf.float32)
arg_2 = tf.constant(-3.5, shape=[1], dtype=tf.float32)
arg_3 = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.QuantizeAndDequantizeV3(input=arg_0, input_min=arg_1, input_max=arg_2, num_bits=arg_3)