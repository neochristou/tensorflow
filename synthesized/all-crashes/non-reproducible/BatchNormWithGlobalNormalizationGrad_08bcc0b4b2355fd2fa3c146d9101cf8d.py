# 2022-04-07 20:01:16.242622: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:01:16.244937: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-04-07 20:01:16.246050: W tensorflow/core/framework/op_kernel.cc:1669] OP_REQUIRES failed at op_kernel.cc:116 : Unimplemented: Op BatchNormWithGlobalNormalizationGrad is not available in GraphDef version 808. It has been removed in version 9. Use tf.nn.batch_normalization().Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/BatchNormWithGlobalNormalizationGrad_08bcc0b4b2355fd2fa3c146d9101cf8d.py", line 12, in <module>    tf.raw_ops.BatchNormWithGlobalNormalizationGrad(t=t, m=m, v=v, gamma=gamma, backprop=backprop, variance_epsilon=variance_epsilon, scale_after_normalization=scale_after_normalization)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_nn_ops.py", line 595, in batch_norm_with_global_normalization_grad    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.UnimplementedError: Op BatchNormWithGlobalNormalizationGrad is not available in GraphDef version 808. It has been removed in version 9. Use tf.nn.batch_normalization(). [Op:BatchNormWithGlobalNormalizationGrad]

# BatchNormGradOp

import tensorflow as tf

variance_epsilon = 0.001
scale_after_normalization = True
t = tf.constant(-1.5e+300, shape=[5,13,5,2], dtype=tf.float64)
m = tf.constant(0.81185869772053976, shape=[5], dtype=tf.float64)
v = tf.constant(0.81185869772053976, shape=[5], dtype=tf.float64)
gamma = tf.constant(0.81185869772053976, shape=[5], dtype=tf.float64)
backprop = tf.constant(0.417022004702574, shape=[3,5,4,5], dtype=tf.float64)
tf.raw_ops.BatchNormWithGlobalNormalizationGrad(t=t, m=m, v=v, gamma=gamma, backprop=backprop, variance_epsilon=variance_epsilon, scale_after_normalization=scale_after_normalization)
