# RandomShuffleOp

import tensorflow as tf

seed = 1066
seed2 = 2021
value = tf.constant(0, shape=[5], dtype=tf.int32)
tf.raw_ops.RandomShuffle(value=value, seed=seed, seed2=seed2)
