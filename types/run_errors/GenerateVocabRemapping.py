# GenerateVocabRemappingOp

import tensorflow as tf

new_vocab_offset = 0
num_new_vocab = 3
old_vocab_size = -1
new_vocab_file = tf.constant("/tmp/checkpoint_ops_test4rspd7es/tmp3rgqxbh2/keyword.txt", shape=[], dtype=tf.string)
old_vocab_file = tf.constant("/tmp/checkpoint_ops_test4rspd7es/tmp3rgqxbh2/keyword.txt", shape=[], dtype=tf.string)
tf.raw_ops.GenerateVocabRemapping(new_vocab_file=new_vocab_file, old_vocab_file=old_vocab_file, new_vocab_offset=new_vocab_offset, num_new_vocab=num_new_vocab, old_vocab_size=old_vocab_size)
