# 2022-01-20 07:05:40.252545: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:05:40.254837: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/SerializeManySparse_665546cd0c44ec74dccb5c24df11bc87.py", line 6, in <module>    tf.raw_ops.SerializeManySparse(sparse_indices=arg_0, sparse_values=arg_1, sparse_shape=arg_2)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/ops/gen_sparse_ops.py", line 496, in serialize_many_sparse    _ops.raise_from_not_ok_status(e, name)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Input shape should be a vector but received shape [] [Op:SerializeManySparse]

import tensorflow as tf

arg_0 = tf.constant(0, shape=[10,3], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float32)
arg_2 = tf.constant(8608480567731124087, shape=[], dtype=tf.int64)
tf.raw_ops.SerializeManySparse(sparse_indices=arg_0, sparse_values=arg_1, sparse_shape=arg_2)