# MapUnstageNoKeyOp

import tensorflow as tf

dtypes = [tf.int32]
capacity = 3
memory_limit = 0
container = ""
shared_name = "MapStagingArea"
indices = tf.constant(-536870912, shape=[1], dtype=tf.int32)
tf.raw_ops.MapUnstageNoKey(indices=indices, dtypes=dtypes, capacity=capacity, memory_limit=memory_limit, container=container, shared_name=shared_name)