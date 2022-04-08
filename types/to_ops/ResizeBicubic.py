# ResizeBicubicOp

import tensorflow as tf

align_corners = False
half_pixel_centers = False
images = tf.constant(12812864, shape=[1,6,6,1], dtype=tf.uint8)
size = tf.constant([8,8], shape=[2], dtype=tf.int32)
tf.raw_ops.ResizeBicubic(images=images, size=size, align_corners=align_corners, half_pixel_centers=half_pixel_centers)
