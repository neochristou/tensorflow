# 2022-02-15 18:04:07.968124: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/QuantizedConv2D_462ca3a74433fd772651270348086953.py", line 9, in <module>    tf.raw_ops.QuantizedConv2D(input=input, filter=filter, min_input=min_input, max_input=max_input, min_filter=min_filter, max_filter=max_filter)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: quantized_conv2d() missing 2 required positional arguments: 'strides' and 'padding'

import tensorflow as tf

input = tf.constant(1, shape=[1, 2, 3, 3], dtype=tf.quint8)
filter = tf.constant(1, shape=[1, 2, 3, 3], dtype=tf.quint8)
min_input = tf.constant([], shape=[0], dtype=tf.float32)
max_input = tf.constant(0, shape=[], dtype=tf.float32)
min_filter = tf.constant(0, shape=[], dtype=tf.float32)
max_filter = tf.constant(0, shape=[], dtype=tf.float32)
tf.raw_ops.QuantizedConv2D(input=input, filter=filter, min_input=min_input,
                           max_input=max_input, min_filter=min_filter, max_filter=max_filter)
