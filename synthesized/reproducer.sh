#!/bin/bash

TIMEOUT_DUR=30
subdirs=("segfault" "fpe" "abort" "other")

do_usage()
{
    echo "Usage: ./`basename $0` --repro <synth_folder> [--clean]"
}

do_clean()
{
    synth_dir=$1
    for subd in ${subdirs[@]}; do
        rm $synth_dir/reproducible/$subd/* || true
    done

    rm $synth_dir/non-reproducible/* || true
}

do_reproduce()
{
    synth_dir=$1
    FILES=$(ls -1 -d $PWD/$synth_dir/all/*.py)
    for f in $FILES; do
        echo $f
        # Kill after TIMEOUT_DUR seconds
        output=$(timeout $TIMEOUT_DUR python3 $f 2>&1)
        exit_code=$?
        fname=$(basename $f)
        # Categorize crashes based on the exit code
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
            out_path="$PWD/$synth_dir/reproducible/$repr_folder"
        else
            out_path="$PWD/$synth_dir/non-reproducible/"
        fi
        output=${output//$'\n'/}
        cp $f $out_path
        # Append the output message
        sed -i "1i# $output\n" "$out_path/$fname"
    done
}

main()
{

    clean=0

    while [[ $# -gt 0 ]]; do
        key="$1"
        case $key in
        --repro)
            shift
            synth_folder=$1
            shift
            ;;
        --clean)
            clean=1
            shift
            ;;
        *)
            do_usage
            exit 1
            ;;
        esac
    done

    [[ $clean -eq 1 ]] && do_clean $synth_folder
    do_reproduce $synth_folder

}

main $@
