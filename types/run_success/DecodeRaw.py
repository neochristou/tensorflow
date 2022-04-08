# DecodeRawOp

import tensorflow as tf

out_type = tf.uint8
little_endian = True
bytes = tf.constant("[string1,string2]", shape=[2], dtype=tf.string)
tf.raw_ops.DecodeRaw(bytes=bytes, out_type=out_type, little_endian=little_endian)
