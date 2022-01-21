# Signal -11;2022-01-20 07:04:00.124562: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMATo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.2022-01-20 07:04:00.126470: I tensorflow/core/common_runtime/process_util.cc:146] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.2022-01-20 07:04:00.127546: W tensorflow/core/kernels/image/non_max_suppression_op.cc:954] Detected a large value for `max_total_size`. This may cause OOM error. (max_total_size: 1879048192)

import tensorflow as tf

arg_0 = tf.constant(0, shape=[1,1,6,4], dtype=tf.float32)
arg_1 = tf.constant(0.9, shape=[1,1,6], dtype=tf.float32)
arg_2 = tf.constant(65534, shape=[], dtype=tf.int32)
arg_3 = tf.constant(1879048192, shape=[], dtype=tf.int32)
arg_4 = tf.constant(0, shape=[], dtype=tf.float32)
arg_5 = tf.constant(0.5, shape=[], dtype=tf.float32)
tf.raw_ops.CombinedNonMaxSuppression(boxes=arg_0, scores=arg_1, max_output_size_per_class=arg_2, max_total_size=arg_3, iou_threshold=arg_4, score_threshold=arg_5)