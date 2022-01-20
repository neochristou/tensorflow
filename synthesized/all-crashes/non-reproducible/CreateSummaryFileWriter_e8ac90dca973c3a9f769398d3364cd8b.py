#   File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/CreateSummaryFileWriter_e8ac90dca973c3a9f769398d3364cd8b.py", line 3    arg_0 = tf.constant(?, shape=[], dtype=tf.resource)                        ^SyntaxError: invalid syntax

import tensorflow as tf

arg_0 = tf.constant(?, shape=[], dtype=tf.resource)
arg_1 = tf.constant("aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaac", shape=[], dtype=tf.string)
arg_2 = tf.constant(10, shape=[], dtype=tf.int32)
arg_3 = tf.constant(10, shape=[], dtype=tf.int32)
arg_4 = tf.constant("/tmp/summary_ops_testutcghtnf/tmpa0w3wnz6", shape=[], dtype=tf.string)
tf.raw_ops.CreateSummaryFileWriter(writer=arg_0, logdir=arg_1, max_queue=arg_2, flush_millis=arg_3, filename_suffix=arg_4)