# Signal -6;2022-04-07 20:02:05.403851: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:05.406163: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:02:05.484727: F tensorflow/core/kernels/maxpooling_op.cc:1032] Check failed: grad_out_index >= output_start && grad_out_index < output_end Invalid output gradient index: 13, 0, 8

# MaxPoolingGradWithArgmaxOp

import tensorflow as tf

ksize = [1, 2, 2, 1]
strides = [1, 1, 1, 1]
padding = "VALID"
include_batch_in_index = False
input = tf.constant(111213, shape=[2,2,2,1], dtype=tf.float32)
grad = tf.constant(111, shape=[2,3,3,1], dtype=tf.float32)
argmax = tf.constant(13, shape=[2,2,2,1], dtype=tf.int64)
tf.raw_ops.MaxPoolGradWithArgmax(input=input, grad=grad, argmax=argmax, ksize=ksize, strides=strides, padding=padding, include_batch_in_index=include_batch_in_index)
