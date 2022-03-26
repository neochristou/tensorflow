# ShardedFilenameOp

import tensorflow as tf

basename = tf.constant("aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaac", shape=[], dtype=tf.string)
shard = tf.constant([], shape=[0], dtype=tf.int32)
num_shards = tf.constant(536870912, shape=[18,22,19,5], dtype=tf.int32)
tf.raw_ops.ShardedFilename(basename=basename, shard=shard, num_shards=num_shards)