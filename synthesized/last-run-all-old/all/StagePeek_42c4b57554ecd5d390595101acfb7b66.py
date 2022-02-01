import tensorflow as tf

index = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.StagePeek(index=index)