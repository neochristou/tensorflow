# 2022-02-15 18:03:51.071849: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/DepthwiseConv2dNativeBackpropFilter_26ecde771509b305b7cc285e0b4549f8.py", line 6, in <module>    tf.raw_ops.DepthwiseConv2dNativeBackpropFilter(input=input, filter_sizes=filter_sizes, out_backprop=out_backprop)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: depthwise_conv2d_native_backprop_filter() missing 2 required positional arguments: 'strides' and 'padding'

import tensorflow as tf

input = tf.constant(1, shape=[1, 4, 4, 3], dtype=tf.float32)
filter_sizes = tf.constant(1879048192, shape=[13], dtype=tf.int32)
out_backprop = tf.constant(1, shape=[1, 4, 4, 3], dtype=tf.float32)
tf.raw_ops.DepthwiseConv2dNativeBackpropFilter(
    input=input, filter_sizes=filter_sizes, out_backprop=out_backprop, strides=[1, 1, 1, 1], padding="SAME")
