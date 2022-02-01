import tensorflow as tf

indices = tf.constant(-536870912, shape=[1], dtype=tf.int32)
tf.raw_ops.MapUnstageNoKey(indices=indices)