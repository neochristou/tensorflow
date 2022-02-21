# 2022-02-15 18:04:14.316825: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/SaveV2_cb92b17e9b0937d2ea341e6848a25af6.py", line 8, in <module>    tf.raw_ops.SaveV2(prefix=prefix, tensor_names=tensor_names, shape_and_slices=shape_and_slices, tensors=tensors, name=name)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_io_ops.py", line 1692, in save_v2    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: <exception str() failed>

import tensorflow as tf

prefix = tf.constant("-00000", shape=[], dtype=tf.string)
tensor_names = tf.constant("[]", shape=[2], dtype=tf.string)
shape_and_slices = tf.constant("[]", shape=[2], dtype=tf.string)
tensors = tf.constant([], shape=[0,2], dtype=tf.complex128)
name = tf.constant("-00000", shape=[], dtype=tf.string)
tf.raw_ops.SaveV2(prefix=prefix, tensor_names=tensor_names, shape_and_slices=shape_and_slices, tensors=tensors, name=name)