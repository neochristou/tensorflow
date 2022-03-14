#!/bin/bash

# set -x

TF_KERNELS_PATH="/media/ivysyn/tensorflow/tensorflow/core/kernels"
INCLUDE_OP_STRING="#include \"tensorflow/core/framework/op_kernel.h\""
INCLUDE_EIGEN_STRING="#define EIGEN_USE"

filenames=$(/usr/bin/fdfind -t f '.*\.cc$|.*\.h$' $TF_KERNELS_PATH --ignore-file inject-ignore)
filenames+=('reshape_op.h')
extra_header_files=("cwise_ops_common.h" "cwise_ops_gpu_common.cu.h" "function_ops.h" "data/experimental/compute_batch_size_op.cc" "shape_ops.h" "conditional_accumulator_base.h" "tensor_to_hash_bucket_op.h" "example_parsing_ops.cc" "string_to_hash_bucket_op.h")

inject_header() {
    filename=$1
    includeopline=$(grep -n "$INCLUDE_OP_STRING" "$filename")
    # Find an appropriate insertion point for the fuzzing header
    # (either after the #include op_kernel line or after the
    # #define EIGEN_USE line to avoid conflicts)
    if [[ ! $includeopline ]]; then
        includeopline=$(grep -n "$INCLUDE_EIGEN_STRING" "$filename")
    fi

    # if [[ ! $includeopline ]]; then
    #     includeopline=$(grep -n "#include" "$filename" | tail -1)
    # fi

    # Edge case
    # If no proper spot found, don't include the header and skip
    if [[ $includeopline ]]; then
        includelineno=$(echo "$includeopline" | cut -f 1 -d ':' | head -1)
        [[ `basename $filename` == "eigen_benchmark_cpu_test.cc" ]] && includelineno=$((includelineno+2))
        sed  -i "$(($includelineno + 1)) i #include \"tensorflow/core/framework/fuzzing.h\"" $filename
    fi
}

main()
{
    for filename in $filenames; do
        echo $filename
        bin/inject-fuzzer --extra-arg-before='-xc++' $filename -- 2> /dev/null | grep 'Successfully' && inject_header $filename # && echo $filename

    done

    # Manually inject fuzzing header in some common header files

    for file in "${extra_header_files[@]}"; do
        filename="$TF_KERNELS_PATH/$file"
        includeopline=$(grep -n "$INCLUDE_OP_STRING" "$filename")
        if [[ ! $includeopline ]]; then
            includeopline=$(grep -n "$INCLUDE_EIGEN_STRING" "$filename")
        fi
        if [[ ! $includeopline ]]; then
            includeoplineno=1
        fi
        includelineno=$(echo "$includeopline" | cut -f 1 -d ':' | head -1)
        sed  -i "$(($includelineno + 1)) i #include \"tensorflow/core/framework/fuzzing.h\"" $filename
    done
}

main
