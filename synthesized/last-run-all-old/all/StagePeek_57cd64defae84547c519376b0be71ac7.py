import tensorflow as tf

index = tf.constant(-536870912, shape=[], dtype=tf.int32)
tf.raw_ops.StagePeek(index=index)