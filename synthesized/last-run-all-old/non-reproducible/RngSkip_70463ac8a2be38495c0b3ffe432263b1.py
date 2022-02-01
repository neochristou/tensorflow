# 2022-01-28 15:27:04.162055: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/RngSkip_70463ac8a2be38495c0b3ffe432263b1.py", line 4, in <module>    tf.raw_ops.RngSkip(resource=resource)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)TypeError: rng_skip() missing 2 required positional arguments: 'algorithm' and 'delta'

import tensorflow as tf

resource = tf.constant(1, shape=[], dtype=tf.int32)
tf.raw_ops.RngSkip(resource=resource)