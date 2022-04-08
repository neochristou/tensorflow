# Signal -6;2022-04-07 20:02:39.312663: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:39.314958: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:02:39.316691: F tensorflow/core/framework/tensor.cc:681] Check failed: 1 == NumElements() (1 vs. 0)Must have a one element tensor

# QuantizeAndDequantizeV3Op

import tensorflow as tf

signed_input = True
range_given = False
narrow_range = False
axis = -1
input = tf.constant(-3.5, shape=[1], dtype=tf.float32)
input_min = tf.constant(-3.5, shape=[1], dtype=tf.float32)
input_max = tf.constant(-3.5, shape=[1], dtype=tf.float32)
num_bits = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.QuantizeAndDequantizeV3(input=input, input_min=input_min, input_max=input_max, num_bits=num_bits, signed_input=signed_input, range_given=range_given, narrow_range=narrow_range, axis=axis)
