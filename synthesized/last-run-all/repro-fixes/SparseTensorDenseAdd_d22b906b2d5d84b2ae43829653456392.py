# 2022-01-21 09:20:18.295905: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-21 09:20:18.299230: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-21 09:20:18.300952: W tensorflow/core/framework/op_kernel.cc:1692] OP_REQUIRES failed at sparse_tensor_dense_add_op.cc:81 : Invalid argument: Dimension 1 does not equal (no broadcasting is supported): sparse side 6 vs dense side 12Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/last-run-all/all/SparseTensorDenseAdd_d22b906b2d5d84b2ae43829653456392.py", line 7, in <module>    tf.raw_ops.SparseTensorDenseAdd(a_indices=arg_0, a_values=arg_1, a_shape=arg_2, b=arg_3)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/ops/gen_sparse_ops.py", line 2968, in sparse_tensor_dense_add    _ops.raise_from_not_ok_status(e, name)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Dimension 1 does not equal (no broadcasting is supported): sparse side 6 vs dense side 12 [Op:SparseTensorDenseAdd]

import tensorflow as tf

arg_0 = tf.constant(0, shape=[17, 2], dtype=tf.int64)
arg_1 = tf.constant([], shape=[0], dtype=tf.float32)
arg_2 = tf.constant([6, 12], shape=[2], dtype=tf.int64)
arg_3 = tf.constant(-0.223668531, shape=[6, 12], dtype=tf.float32)
tf.raw_ops.SparseTensorDenseAdd(
    a_indices=arg_0, a_values=arg_1, a_shape=arg_2, b=arg_3)
