# SummaryAudioOp

import tensorflow as tf

max_outputs = 3
tag = tf.constant("snd", shape=[], dtype=tf.string)
tensor = tf.constant(-0.847383440.55983758, shape=[4,7,1], dtype=tf.float32)
sample_rate = tf.constant(8000, shape=[], dtype=tf.float32)
tf.raw_ops.AudioSummary(tag=tag, tensor=tensor, sample_rate=sample_rate, max_outputs=max_outputs)
