#!/bin/sh
SETCOLOR_FAILURE="echo \\033[1;31m"
SETCOLOR_NORMAL="echo \\033[0;39m"
SETCOLOR_EXAMPLE="echo \\033[1;32m"

if  [ ! $1 ] || [ ! $2 ] ; then
${SETCOLOR_FAILURE}
echo "FAILURE!!!";
${SETCOLOR_NORMAL}
echo "\$1 - file_to_read.csv
\$2 - column name"
${SETCOLOR_EXAMPLE}
echo "EXAMPLE"
${SETCOLOR_NORMAL}
echo "sh counter.sh hh_positions.csv name";
    exit 1;
fi;

FILE_NAME="hh_uniq_positions.csv"

echo "\"$2\",\"count\"" > $FILE_NAME;