# 2022-01-31 21:30:25.964089: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.Traceback (most recent call last):  File "/media/mlfuzz/tensorflow/synthesized/last-run-all/all/LSTMBlockCell_3aca927766ea6e29fbcdff3715f72781.py", line 11, in <module>    tf.raw_ops.LSTMBlockCell(x=x, cs_prev=cs_prev, h_prev=h_prev, w=w, wci=wci, wcf=wcf, wco=wco, b=b)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_rnn_ops.py", line 881, in lstm_block_cell    return lstm_block_cell_eager_fallback(  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/ops/gen_rnn_ops.py", line 931, in lstm_block_cell_eager_fallback    _result = _execute.execute(b"LSTMBlockCell", 7, inputs=_inputs_flat,  File "/media/fuzzing-pytorch/anaconda3/lib/python3.8/site-packages/tensorflow/python/eager/execute.py", line 59, in quick_execute    tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,tensorflow.python.framework.errors_impl.InvalidArgumentError: cs_prev.dims(0) != batch_size: 14 vs. 22 [Op:LSTMBlockCell]

import tensorflow as tf

x = tf.constant(3.5e+35, shape=[22], dtype=tf.float32)
cs_prev = tf.constant(-3.5e+35, shape=[14,4], dtype=tf.float32)
h_prev = tf.constant(0, shape=[], dtype=tf.float32)
w = tf.constant(3.5e+35, shape=[2,16,22,16], dtype=tf.float32)
wci = tf.constant(-3.5e+35, shape=[17], dtype=tf.float32)
wcf = tf.constant(0, shape=[17], dtype=tf.float32)
wco = tf.constant(0, shape=[17], dtype=tf.float32)
b = tf.constant(0.837607, shape=[28,29], dtype=tf.float32)
tf.raw_ops.LSTMBlockCell(x=x, cs_prev=cs_prev, h_prev=h_prev, w=w, wci=wci, wcf=wcf, wco=wco, b=b)