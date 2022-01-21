# 2022-01-20 07:04:01.042389: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:04:01.044530: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/Conv3DBackpropFilter_19c87d72048870caf4d4ab3e6542b062.py", line 6, in <module>    tf.raw_ops.Conv3DBackpropFilter(input=arg_0, filter=arg_1, out_backprop=arg_2)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: conv3d_backprop_filter() missing 2 required positional arguments: 'strides' and 'padding'

import tensorflow as tf

arg_0 = tf.constant(-64992, shape=[2,5,4,3,2], dtype=tf.float16)
arg_1 = tf.constant(0, shape=[], dtype=tf.int32)
arg_2 = tf.constant(0, shape=[2,5,4,3,2], dtype=tf.float16)
tf.raw_ops.Conv3DBackpropFilter(input=arg_0, filter=arg_1, out_backprop=arg_2)