# 2022-02-15 18:03:47.765929: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/Conv3DBackpropFilter_41ad12b93fac8fb63c4f587c7eb395c2.py", line 6, in <module>    tf.raw_ops.Conv3DBackpropFilter(input=input, filter=filter, out_backprop=out_backprop)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: conv3d_backprop_filter() missing 2 required positional arguments: 'strides' and 'padding'

import tensorflow as tf

input = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
filter = tf.constant(0, shape=[], dtype=tf.int32)
out_backprop = tf.constant(.5053710941, shape=[2,2,2,2,1], dtype=tf.float16)
tf.raw_ops.Conv3DBackpropFilter(input=input, filter=filter, out_backprop=out_backprop)