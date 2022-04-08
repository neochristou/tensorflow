# 2022-04-07 20:02:57.173756: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:02:57.175941: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/SaveV2_451c71789269667d281dfc5598da1ddc.py", line 9, in <module>    tf.raw_ops.SaveV2(prefix=prefix, tensor_names=tensor_names, shape_and_slices=shape_and_slices, tensors=tensors)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_io_ops.py", line 1692, in save_v2    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Length for attr 'dtypes' of 0 must be at least minimum 1	; NodeDef: {{node SaveV2}}; Op<name=SaveV2; signature=prefix:string, tensor_names:string, shape_and_slices:string, tensors: -> ; attr=dtypes:list(type),min=1; is_stateful=true> [Op:SaveV2]

# SaveV2

import tensorflow as tf

prefix = tf.constant("-00000", shape=[], dtype=tf.string)
tensor_names = tf.constant("[]", shape=[2], dtype=tf.string)
shape_and_slices = tf.constant("[]", shape=[2], dtype=tf.string)
tensors = tf.constant([], shape=[0, 2], dtype=tf.complex128)
tf.raw_ops.SaveV2(prefix=prefix, tensor_names=tensor_names,
                  shape_and_slices=shape_and_slices, tensors=tensors)
