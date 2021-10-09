#!/bin/bash

TF_KERNELS_PATH="/media/tf-fuzzing/tensorflow/tensorflow/core/kernels"
INCLUDE_OP_STRING="#include \"tensorflow/core/framework/op_kernel.h\""

filenames=$(/usr/bin/fdfind -t f '.*\.cc$' $TF_KERNELS_PATH)

for filename in $filenames; do
    includeopline=$(grep -n "$INCLUDE_OP_STRING" "$filename")
    # If it doesn't include the OP kernel header, it probably isn't a kernel
    if [[ ! $includeopline ]]; then
        continue
    fi
    includelineno=$(echo "$includeopline" | cut -f 1 -d ':' | head -1)
    sed  -i "$(($includelineno + 1)) i #include \"tensorflow/core/framework/fuzzing.h\"" $filename
    bin/inject-fuzzer $filename --
done

