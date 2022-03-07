# 2022-03-04 18:44:44.665970: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/FusedBatchNormV3_3390cda59153492c3fa46ee935eeace2.py", line 14, in <module>    tf.raw_ops.FusedBatchNormV3(x=x, scale=scale, offset=offset, mean=mean, variance=variance, epsilon=epsilon, exponential_avg_factor=exponential_avg_factor, data_format=data_format, is_training=is_training)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_nn_ops.py", line 4274, in fused_batch_norm_v3    return fused_batch_norm_v3_eager_fallback(  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/ops/gen_nn_ops.py", line 4336, in fused_batch_norm_v3_eager_fallback    _result = _execute.execute(b"FusedBatchNormV3", 6, inputs=_inputs_flat,  File "/media/anaconda3/envs/ivysyn/lib/python3.9/site-packages/tensorflow/python/eager/execute.py", line 59, in quick_execute    tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,tensorflow.python.framework.errors_impl.InvalidArgumentError: scale must have the same number of elements as the channels of x, got 0 and 6 [Op:FusedBatchNormV3]

# FusedBatchNormOpV3

import tensorflow as tf

epsilon = 0.001
exponential_avg_factor = 1
data_format = "NCHW"
is_training = True
x = tf.constant(00, shape=[1,6,4,1], dtype=tf.float32)
scale = tf.constant([], shape=[0], dtype=tf.float32)
offset = tf.constant(1, shape=[6], dtype=tf.float32)
mean = tf.constant([], shape=[0], dtype=tf.float32)
variance = tf.constant(1, shape=[6], dtype=tf.float32)
tf.raw_ops.FusedBatchNormV3(x=x, scale=scale, offset=offset, mean=mean, variance=variance, epsilon=epsilon, exponential_avg_factor=exponential_avg_factor, data_format=data_format, is_training=is_training)