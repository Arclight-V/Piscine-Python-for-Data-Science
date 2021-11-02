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
echo "sh concatenator.sh .csv";
    exit 1;
fi;


FILE_NAME="hh_positions.csv"
HEADER=$(head -n 1 $1)


echo $HEADER > $FILE_NAME
cat *.csv | sed  -En '/^"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"$/!p'  >> $FILE_NAME