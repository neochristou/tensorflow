# 2022-02-15 18:04:26.104117: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-02-15 18:04:26.108935: W tensorflow/core/framework/op_kernel.cc:1692] OP_REQUIRES failed at sparse_tensor_dense_add_op.cc:81 : Invalid argument: Dimension 1 does not equal (no broadcasting is supported): sparse side 6 vs dense side 12Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/SparseTensorDenseAdd_0d1514c611708b251a087d2a2f93df2f.py", line 7, in <module>    tf.raw_ops.SparseTensorDenseAdd(a_indices=a_indices, a_values=a_values, a_shape=a_shape, b=b)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_sparse_ops.py", line 2968, in sparse_tensor_dense_add    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Dimension 1 does not equal (no broadcasting is supported): sparse side 6 vs dense side 12 [Op:SparseTensorDenseAdd]

import tensorflow as tf

a_indices = tf.constant(0, shape=[17, 2], dtype=tf.int64)
a_values = tf.constant([], shape=[0], dtype=tf.float32)
a_shape = tf.constant(6, shape=[2], dtype=tf.int64)
b = tf.constant(-0.223668531, shape=[6, 12], dtype=tf.float32)
tf.raw_ops.SparseTensorDenseAdd(
    a_indices=a_indices, a_values=a_values, a_shape=a_shape, b=b)
