# Signal -6;2022-01-20 07:04:12.443911: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:04:12.446064: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-20 07:04:12.446918: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 6)Must have a one element tensor

import tensorflow as tf

arg_0 = tf.constant(-3.5e+35, shape=[2,3], dtype=tf.float32)
arg_1 = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
arg_2 = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
arg_3 = tf.constant(0.898730755, shape=[2,3], dtype=tf.float32)
tf.raw_ops.FakeQuantWithMinMaxVarsGradient(gradients=arg_0, inputs=arg_1, min=arg_2, max=arg_3)