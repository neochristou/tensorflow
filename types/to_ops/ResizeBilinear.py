# ResizeBilinearOp

import tensorflow as tf

align_corners = False
half_pixel_centers = False
images = tf.constant(1, shape=[1,2,3,2], dtype=tf.float32)
size = tf.constant([12,4], shape=[2], dtype=tf.int32)
tf.raw_ops.ResizeBilinear(images=images, size=size, align_corners=align_corners, half_pixel_centers=half_pixel_centers)
