# DebugIdentityV2Op

import tensorflow as tf

tfdbg_context_id = "deadbeaf"
op_name = "x"
output_slot = 0
tensor_debug_mode = 7
debug_urls = ["file:///tmp/tmp57d4oz7z"]
circular_buffer_size = 1000
tfdbg_run_id = ""
input = tf.constant(10, shape=[], dtype=tf.int32)
tf.raw_ops.DebugIdentityV2(input=input, tfdbg_context_id=tfdbg_context_id, op_name=op_name, output_slot=output_slot, tensor_debug_mode=tensor_debug_mode, debug_urls=debug_urls, circular_buffer_size=circular_buffer_size, tfdbg_run_id=tfdbg_run_id)
