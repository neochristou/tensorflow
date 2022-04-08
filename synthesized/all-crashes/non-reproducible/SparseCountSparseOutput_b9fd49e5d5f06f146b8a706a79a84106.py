# 2022-04-07 20:03:04.833285: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:04.835192: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/SparseCountSparseOutput_b9fd49e5d5f06f146b8a706a79a84106.py", line 12, in <module>    tf.raw_ops.SparseCountSparseOutput(indices=indices, values=values, dense_shape=dense_shape, weights=weights, binary_output=binary_output, minlength=minlength, maxlength=maxlength)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_count_ops.py", line 276, in sparse_count_sparse_output    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Input indices must be a 2-dimensional tensor. Got: [7] [Op:SparseCountSparseOutput]

# SparseCount

import tensorflow as tf

binary_output = False
minlength = 6
maxlength = 6
indices = tf.constant(1879048192, shape=[7], dtype=tf.int64)
values = tf.constant([], shape=[0], dtype=tf.int64)
dense_shape = tf.constant([], shape=[0], dtype=tf.int64)
weights = tf.constant([], shape=[0], dtype=tf.int64)
tf.raw_ops.SparseCountSparseOutput(indices=indices, values=values, dense_shape=dense_shape, weights=weights, binary_output=binary_output, minlength=minlength, maxlength=maxlength)
