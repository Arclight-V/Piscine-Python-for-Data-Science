#!/bin/sh
SETCOLOR_FAILURE="echo \\033[1;31m"
SETCOLOR_NORMAL="echo \\033[0;39m"
SETCOLOR_EXAMPLE="echo \\033[1;32m"

if  [ ! $1 ] || [ ! $2 ]; then
${SETCOLOR_FAILURE}
echo "FAILURE!!!";
${SETCOLOR_NORMAL}
echo "\$1 - python_script.py
\$2 - profiling_file"
${SETCOLOR_EXAMPLE}
echo "EXAMPLE"
${SETCOLOR_NORMAL}
echo "sh financial.py profiling-sleep.txt";
    exit 1;
fi;

script=$1
ticker="FB"
field="Total Revenue"
sort="ncalls"
output_file=$2

python3 -m cProfile -s $sort -m $script $ticker "$field" > $output_file