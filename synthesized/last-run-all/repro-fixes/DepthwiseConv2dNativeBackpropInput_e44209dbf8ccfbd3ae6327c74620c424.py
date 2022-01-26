# 2022-01-21 09:19:21.339169: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-21 09:19:21.342403: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/last-run-all/all/DepthwiseConv2dNativeBackpropInput_e44209dbf8ccfbd3ae6327c74620c424.py", line 6, in <module>    tf.raw_ops.DepthwiseConv2dNativeBackpropInput(input_sizes=arg_0, filter=arg_1, out_backprop=arg_2)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: depthwise_conv2d_native_backprop_input() missing 2 required positional arguments: 'strides' and 'padding'

import tensorflow as tf

arg_0 = tf.constant(1879048192, shape=[13], dtype=tf.int32)
arg_1 = tf.constant(0.184634328, shape=[1, 1, 48, 2], dtype=tf.float32)
arg_2 = tf.constant(0.184634328, shape=[1, 1, 48, 2], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropInput(
    input_sizes=arg_0, filter=arg_1, out_backprop=arg_2, strides=[1, 1, 1, 1], padding="SAME")
