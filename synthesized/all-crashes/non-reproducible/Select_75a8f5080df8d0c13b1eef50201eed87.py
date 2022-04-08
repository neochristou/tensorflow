# 2022-04-07 20:02:58.501881: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:58.504145: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/Select_75a8f5080df8d0c13b1eef50201eed87.py", line 8, in <module>    tf.raw_ops.Select(condition=condition, x=x, y=y)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_math_ops.py", line 8844, in select    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: 'then' and 'else' must have the same size.  but received: [13,24] vs. [18,22,19,5] [Op:Select]

# SelectOp

import tensorflow as tf

condition = tf.constant(False, shape=[], dtype=tf.bool)
x = tf.constant(3.5e+35, shape=[13, 24], dtype=tf.float32)
y = tf.constant(-3.5e+35, shape=[18, 22, 19, 5], dtype=tf.float32)
tf.raw_ops.Select(condition=condition, x=x, y=y)
