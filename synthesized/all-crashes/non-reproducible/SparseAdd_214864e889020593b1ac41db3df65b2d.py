# 2022-01-20 07:05:44.503857: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:05:44.506044: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/SparseAdd_214864e889020593b1ac41db3df65b2d.py", line 10, in <module>    tf.raw_ops.SparseAdd(a_indices=arg_0, a_values=arg_1, a_shape=arg_2, b_indices=arg_3, b_values=arg_4, b_shape=arg_5, thresh=arg_6)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/ops/gen_sparse_ops.py", line 676, in sparse_add    _ops.raise_from_not_ok_status(e, name)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: cannot compute SparseAdd as input #4(zero-based) was expected to be a double tensor but is a int32 tensor [Op:SparseAdd]

import tensorflow as tf

arg_0 = tf.constant(0, shape=[2,2], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float64)
arg_2 = tf.constant([], shape=[0], dtype=tf.int64)
arg_3 = tf.constant(-1879048192, shape=[2,2], dtype=tf.int64)
arg_4 = tf.constant(1, shape=[2], dtype=tf.int32)
arg_5 = tf.constant(0, shape=[2,2], dtype=tf.int64)
arg_6 = tf.constant(1, shape=[2], dtype=tf.int32)
tf.raw_ops.SparseAdd(a_indices=arg_0, a_values=arg_1, a_shape=arg_2, b_indices=arg_3, b_values=arg_4, b_shape=arg_5, thresh=arg_6)