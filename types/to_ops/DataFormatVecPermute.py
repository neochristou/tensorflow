# DataFormatVecPermuteOp

import tensorflow as tf

src_format = "NHWC"
dst_format = "NCHW"
x = tf.constant(1, shape=[4], dtype=tf.int32)
tf.raw_ops.DataFormatVecPermute(x=x, src_format=src_format, dst_format=dst_format)
