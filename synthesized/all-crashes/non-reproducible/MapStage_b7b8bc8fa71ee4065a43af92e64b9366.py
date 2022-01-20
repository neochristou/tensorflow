# 2022-01-20 07:04:38.779046: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:04:38.781133: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/MapStage_b7b8bc8fa71ee4065a43af92e64b9366.py", line 6, in <module>    tf.raw_ops.MapStage(key=arg_0, indices=arg_1, values=arg_2)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: map_stage() missing 1 required positional argument: 'dtypes'

import tensorflow as tf

arg_0 = tf.constant(1879048192, shape=[10,19,22], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float64)
arg_2 = tf.constant([], shape=[0], dtype=tf.float64)
tf.raw_ops.MapStage(key=arg_0, indices=arg_1, values=arg_2)