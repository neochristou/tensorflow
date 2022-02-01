# Wrong type
# 2022-01-31 11:00:41.367860: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/StatelessMultinomial_f34d497dbab2e58e162cd722bc276011.py", line 6, in <module>    tf.raw_ops.StatelessMultinomial(logits=logits, num_samples=num_samples, seed=seed)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_stateless_random_ops.py", line 50, in stateless_multinomial    _ops.raise_from_not_ok_status(e, name)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: logits should be a matrix, got shape [10,19,22] [Op:StatelessMultinomial]

import tensorflow as tf

logits = tf.constant(-3.5e+35, shape=[10, 19, 22], dtype=tf.float32)
num_samples = tf.constant(-536870912, shape=[], dtype=tf.int32)
seed = tf.constant(3852221141, shape=[2], dtype=tf.int64)
tf.raw_ops.StatelessMultinomial(
    logits=logits, num_samples=num_samples, seed=seed)
