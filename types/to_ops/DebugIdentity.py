# DebugIdentityOp

import tensorflow as tf

device_name = ""
tensor_name = "FakeTensor:0"
debug_urls = []
gated_grpc = False
input = tf.constant(1, shape=[6], dtype=tf.int32)
tf.raw_ops.DebugIdentity(input=input, device_name=device_name, tensor_name=tensor_name, debug_urls=debug_urls, gated_grpc=gated_grpc)
