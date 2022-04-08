# CompositeTensorVariantFromComponents

import tensorflow as tf

metadata = "\n
components = tf.constant(1, shape=[1], dtype=tf.int32)
tf.raw_ops.CompositeTensorVariantFromComponents(components=components, metadata=metadata)
