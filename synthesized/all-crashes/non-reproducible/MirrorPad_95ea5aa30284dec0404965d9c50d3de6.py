# 2022-01-20 07:04:39.928254: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:04:39.930379: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/MirrorPad_95ea5aa30284dec0404965d9c50d3de6.py", line 5, in <module>    tf.raw_ops.MirrorPad(input=arg_0, paddings=arg_1)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: mirror_pad() missing 1 required positional argument: 'mode'

import tensorflow as tf

arg_0 = tf.constant([], shape=[0], dtype=tf.float32)
arg_1 = tf.constant(65534, shape=[12,10,19], dtype=tf.int32)
tf.raw_ops.MirrorPad(input=arg_0, paddings=arg_1)