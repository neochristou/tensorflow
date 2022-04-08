# 2022-04-07 20:03:01.127150: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-04-07 20:03:01.129401: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/media/ivysyn/tensorflow/synthesized/all-crashes/all/ShardedFilename_09f6939000a32e0aaaddc1e1cc394116.py", line 8, in <module>    tf.raw_ops.ShardedFilename(basename=basename, shard=shard, num_shards=num_shards)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/ops/gen_io_ops.py", line 1745, in sharded_filename    _ops.raise_from_not_ok_status(e, name)  File "/media/anaconda3/envs/tf-2.6-pkg/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: shard must be a scalar, got shape [0] [Op:ShardedFilename]

# ShardedFilenameOp

import tensorflow as tf

basename = tf.constant("aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaac", shape=[], dtype=tf.string)
shard = tf.constant([], shape=[0], dtype=tf.int32)
num_shards = tf.constant(536870912, shape=[18, 22, 19, 5], dtype=tf.int32)
tf.raw_ops.ShardedFilename(
    basename=basename, shard=shard, num_shards=num_shards)
