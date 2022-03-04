# 2022-03-04 18:44:38.582441: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/DeserializeSparse_c7f4e1afb8b7df191fcad7fcf90f47a4.py", line 7, in <module>    tf.raw_ops.DeserializeSparse(serialized_sparse=serialized_sparse, dtype=dtype)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_sparse_ops.py", line 421, in deserialize_sparse    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Serialized sparse should have 3 as the last dimension [0] [Op:DeserializeSparse]

# DeserializeSparseOp

import tensorflow as tf

dtype = tf.int32
serialized_sparse = tf.constant("[]", shape=[0], dtype=tf.string)
tf.raw_ops.DeserializeSparse(serialized_sparse=serialized_sparse, dtype=dtype)