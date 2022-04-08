# SummaryImageOp

import tensorflow as tf

max_images = 3
bad_color = Tensor<type: uint8 shape: [4] values: 255 0 0...>
tag = tf.constant("img", shape=[], dtype=tf.string)
tensor = tf.constant(-0.636879683, shape=[4,5,7,1], dtype=tf.float32)
tf.raw_ops.ImageSummary(tag=tag, tensor=tensor, max_images=max_images, bad_color=bad_color)
