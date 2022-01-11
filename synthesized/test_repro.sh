#!/bin/bash

FILES=$(ls -1 -d "$PWD/all-crashes/"*)
for f in $FILES; do
	output=$(python3 $f 2>&1)
	exit_code=$?
	fname=$(basename $f)
	if [[ ! $exit_code =~ ^(0|1)$ ]]; then
		repr_folder="reproducible"
		output="Signal $exit_code"
	else
		repr_folder="non-reproducible"
	fi
	cp $f $PWD/$repr_folder/
	output=${output//$'\n'/}
	sed -i "1i# $output\n" $PWD/$repr_folder/$fname
done
