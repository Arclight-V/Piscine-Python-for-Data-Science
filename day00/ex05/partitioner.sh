#!/bin/sh
SETCOLOR_FAILURE="echo \\033[1;31m"
SETCOLOR_NORMAL="echo \\033[0;39m"
SETCOLOR_EXAMPLE="echo \\033[1;32m"

if  [ ! $1 ] ; then
${SETCOLOR_FAILURE}
echo "FAILURE!!!";
${SETCOLOR_NORMAL}
echo "\$1 - file_to_read.csv"
${SETCOLOR_EXAMPLE}
echo "EXAMPLE"
${SETCOLOR_NORMAL}
echo "sh partitioner.sh hh_positions.csv";
    exit 1;
fi;

COLUMN=2

awk -F '\",\"|T' -v col=$COLUMN 'NR==1 {a=$0; next} {b=$col".csv"} !($col in c) {c[$col]; print a > b} {print >> b}' "$1"
