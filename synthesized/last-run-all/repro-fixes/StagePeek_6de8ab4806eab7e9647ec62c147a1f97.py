# 2022-01-21 09:20:20.459525: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-21 09:20:20.462521: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/last-run-all/all/StagePeek_6de8ab4806eab7e9647ec62c147a1f97.py", line 4, in <module>    tf.raw_ops.StagePeek(index=arg_0)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: stage_peek() missing 1 required positional argument: 'dtypes'

import tensorflow as tf

arg_0 = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.StagePeek(index=arg_0, dtypes=[tf.int32])
