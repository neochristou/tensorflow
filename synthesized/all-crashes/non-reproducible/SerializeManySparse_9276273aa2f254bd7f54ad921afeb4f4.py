# 2022-03-07 18:56:01.324600: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/SerializeManySparse_9276273aa2f254bd7f54ad921afeb4f4.py", line 9, in <module>    tf.raw_ops.SerializeManySparse(sparse_indices=sparse_indices, sparse_values=sparse_values, sparse_shape=sparse_shape, out_type=out_type)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_sparse_ops.py", line 496, in serialize_many_sparse    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Input values should be a vector but received shape [] [Op:SerializeManySparse]

# SerializeManySparseOp

import tensorflow as tf

out_type = tf.variant
sparse_indices = tf.constant(0, shape=[3,2], dtype=tf.int64)
sparse_values = tf.constant(1879048192, shape=[], dtype=tf.int32)
sparse_shape = tf.constant([], shape=[0], dtype=tf.int64)
tf.raw_ops.SerializeManySparse(sparse_indices=sparse_indices, sparse_values=sparse_values, sparse_shape=sparse_shape, out_type=out_type)