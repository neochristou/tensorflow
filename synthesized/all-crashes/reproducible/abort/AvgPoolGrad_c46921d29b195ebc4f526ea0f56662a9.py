# Signal -6;2022-04-07 20:01:13.851664: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:13.854000: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:13.856520: F tensorflow/core/framework/tensor_shape.cc:397] Check failed: size >= 0 (-536870912 vs. 0)

# AvgPoolingGradOp

import tensorflow as tf

ksize = [1, 1, 1, 1]
strides = [1, 1, 1, 1]
padding = "VALID"
data_format = "NHWC"
orig_input_shape = tf.constant(-536870912, shape=[4], dtype=tf.int32)
grad = tf.constant(1, shape=[2,1,5,2], dtype=tf.float32)
tf.raw_ops.AvgPoolGrad(orig_input_shape=orig_input_shape, grad=grad, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
