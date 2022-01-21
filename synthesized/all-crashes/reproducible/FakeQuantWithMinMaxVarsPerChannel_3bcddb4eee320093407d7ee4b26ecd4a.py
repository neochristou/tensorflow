# Signal -6;2022-01-20 07:04:14.510069: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:04:14.512496: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-20 07:04:14.513453: F tensorflow/core/framework/tensor_shape.cc:46] Check failed: NDIMS == dims() (1 vs. 4)Asking for tensor of 1 dimensions from a tensor of 4 dimensions

import tensorflow as tf

arg_0 = tf.constant(-3.5e+35, shape=[10,19,22], dtype=tf.float32)
arg_1 = tf.constant(3.5e+35, shape=[22,19,5,13], dtype=tf.float32)
arg_2 = tf.constant(3.5e+35, shape=[22,19,5,13], dtype=tf.float32)
tf.raw_ops.FakeQuantWithMinMaxVarsPerChannel(inputs=arg_0, min=arg_1, max=arg_2)