# 2022-01-20 07:06:16.894442: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:06:16.896612: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.Traceback (most recent call last):  File "/home/neo/mlfuzz/tensorflow/synthesized/all-crashes/all/Substr_131694a33b690e09feeeaa9804c2a4c8.py", line 6, in <module>    tf.raw_ops.Substr(input=arg_0, pos=arg_1, len=arg_2)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/util/tf_export.py", line 404, in wrapper    return f(**kwargs)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/ops/gen_string_ops.py", line 1925, in substr    _ops.raise_from_not_ok_status(e, name)  File "/home/neo/anaconda3/envs/tf/lib/python3.9/site-packages/tensorflow/python/framework/ops.py", line 6941, in raise_from_not_ok_status    six.raise_from(core._status_to_exception(e.code, message), None)  File "<string>", line 3, in raise_fromtensorflow.python.framework.errors_impl.InvalidArgumentError: Value for attr 'T' of double is not in the list of allowed values: int32, int64	; NodeDef: {{node Substr}}; Op<name=Substr; signature=input:string, pos:T, len:T -> output:string; attr=T:type,allowed=[DT_INT32, DT_INT64]; attr=unit:string,default="BYTE",allowed=["BYTE", "UTF8_CHAR"]> [Op:Substr]

import tensorflow as tf

arg_0 = tf.constant("aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaac", shape=[], dtype=tf.string)
arg_1 = tf.constant([], shape=[0], dtype=tf.float64)
arg_2 = tf.constant([], shape=[0], dtype=tf.int32)
tf.raw_ops.Substr(input=arg_0, pos=arg_1, len=arg_2)