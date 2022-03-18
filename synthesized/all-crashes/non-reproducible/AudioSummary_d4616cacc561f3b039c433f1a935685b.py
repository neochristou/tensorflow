# 2022-03-07 18:52:49.570645: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/AudioSummary_d4616cacc561f3b039c433f1a935685b.py", line 9, in <module>    tf.raw_ops.AudioSummary(tag=tag, tensor=tensor, sample_rate=sample_rate, max_outputs=max_outputs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_logging_ops.py", line 122, in audio_summary    return audio_summary_eager_fallback(  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_logging_ops.py", line 149, in audio_summary_eager_fallback    sample_rate = _execute.make_float(sample_rate, "sample_rate")  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/eager/execute.py", line 161, in make_float    raise TypeError("Expected float for argument '%s' not %s." %TypeError: Expected float for argument 'sample_rate' not <tf.Tensor: shape=(5, 3, 4), dtype=float32, numpy=array([[[1., 1., 1., 1.],        [1., 1., 1., 1.],        [1., 1., 1., 1.]],       [[1., 1., 1., 1.],        [1., 1., 1., 1.],        [1., 1., 1., 1.]],       [[1., 1., 1., 1.],        [1., 1., 1., 1.],        [1., 1., 1., 1.]],       [[1., 1., 1., 1.],        [1., 1., 1., 1.],        [1., 1., 1., 1.]],       [[1., 1., 1., 1.],        [1., 1., 1., 1.],        [1., 1., 1., 1.]]], dtype=float32)>.

# SummaryAudioOp

import tensorflow as tf

max_outputs = 3
tag = tf.constant("outer/inner", shape=[], dtype=tf.string)
tensor = tf.constant(1, shape=[5,3,4], dtype=tf.float32)
sample_rate = tf.constant(1, shape=[5,3,4], dtype=tf.float32)
tf.raw_ops.AudioSummary(tag=tag, tensor=tensor, sample_rate=sample_rate, max_outputs=max_outputs)