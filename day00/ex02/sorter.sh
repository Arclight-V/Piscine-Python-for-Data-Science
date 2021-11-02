#!/bin/sh
SETCOLOR_FAILURE="echo \\033[1;31m"
SETCOLOR_NORMAL="echo \\033[0;39m"
SETCOLOR_EXAMPLE="echo \\033[1;32m"


if  [ ! $1 ] || [ ! $2 ] ; then
${SETCOLOR_FAILURE}
echo "FAILURE!!!";
${SETCOLOR_NORMAL}
echo "\$1 - hh.csv
\$2 - hh_sorted.csv"
${SETCOLOR_EXAMPLE}
echo "EXAMPLE"
${SETCOLOR_NORMAL}
echo "sh sorter.sh hh.csv hh_sorted.csv \\n";
    exit 1;
fi;

head -n 1 $1 > $2 && tail -n +2 $1 | sort -t"," -nk2 -k1 >> $2