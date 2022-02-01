#!/bin/bash

crash_dir=$1
TIMEOUT_DUR=30

FILES=$(ls -1 -d $PWD/$crash_dir/all/*.py)
for f in $FILES; do
    echo $f
	output=$(timeout $TIMEOUT_DUR python3 $f 2>&1)
	exit_code=$?
	fname=$(basename $f)
	if [[ ! $exit_code =~ ^(0|1)$ ]]; then
        sig=$(($exit_code - 128))
        case $sig in
            '11')
                repr_folder="segfault"
                ;;
            '8')
                repr_folder="fpe"
                ;;
            '6')
                repr_folder="abort"
                ;;
            *)
                repr_folder="other"
                ;;
        esac
		output="Signal -$sig;$output"
        out_path="$PWD/$crash_dir/reproducible/$repr_folder"
	else
        out_path="$PWD/$crash_dir/non-reproducible/"
	fi
	output=${output//$'\n'/}
    cp $f $out_path
	sed -i "1i# $output\n" "$out_path/$fname"
done
