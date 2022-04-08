# ComputeAccidentalHitsOp

import tensorflow as tf

num_true = 2
seed = 87654321
seed2 = 979136014
true_classes = tf.constant(1, shape=[3,2], dtype=tf.int64)
sampled_candidates = tf.constant(0, shape=[5], dtype=tf.int64)
tf.raw_ops.ComputeAccidentalHits(true_classes=true_classes, sampled_candidates=sampled_candidates, num_true=num_true, seed=seed, seed2=seed2)
