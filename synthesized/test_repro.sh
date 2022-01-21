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
		repr_folder="$crash_dir/reproducible"
        sig=$(($exit_code - 128))
		output="Signal -$sig;$output"
	else
		repr_folder="$crash_dir/non-reproducible"
	fi
	cp $f $PWD/$repr_folder/
	output=${output//$'\n'/}
	sed -i "1i# $output\n" $PWD/$repr_folder/$fname
done
