import tensorflow as tf

arg_0 = tf.constant("aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaac", shape=[], dtype=tf.string)
arg_1 = tf.constant([], shape=[0], dtype=tf.float64)
arg_2 = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.Substr(input=arg_0, pos=arg_1, len=arg_2)