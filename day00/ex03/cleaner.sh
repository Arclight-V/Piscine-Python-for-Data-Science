#!/bin/sh
SETCOLOR_FAILURE="echo \\033[1;31m"
SETCOLOR_NORMAL="echo \\033[0;39m"
SETCOLOR_EXAMPLE="echo \\033[1;32m"

if  [ ! $1 ] || [ ! $2 ] || [ ! $3 ] ; then
${SETCOLOR_FAILURE}
echo "FAILURE!!!";
${SETCOLOR_NORMAL}
echo "\$1 - file.csv
\$2 - position name
\$3 - replacement word
\$4 - replacement word"
\$5 - replacement word""
${SETCOLOR_EXAMPLE}
echo "EXAMPLE"
${SETCOLOR_NORMAL}
echo "sh cleaner.sh hh_sorted.csv name Junior Middle Senior \\n";
    exit 1;
fi;

FILE_NAME="hh_positions.csv"
REPLACE_FIRST="junior"
REPLACE_SECOND="middle"
REPLACE_THIRD="senior"

str=$(head -n 1 $1)
IFS=", " read -ra ADDR <<< "$str"
column=1
for i in "${ADDR[@]}"; do
    word="${i:1}"
    word=${word%?}
    [[ "$word" == "$2" ]] && break
    ((++column))
done

cleaner()
{
  awk -F',' -v col=$column \
            -v "f_replace=$REPLACE_FIRST" \
            -v "s_replace=$REPLACE_SECOND" \
            -v "t_replace=$REPLACE_THIRD" \
'BEGIN {OFS = FS}
{
    if (tolower($col) ~ "f_replace" && tolower($col) ~ "s_replace" && tolower($col) ~ "t_replace")
    $col = "\"Junior/Middle/Senior\""
  else if (tolower($col) ~ "f_replace" && tolower($col) ~ "s_replace")
    $col = "\"Junior/Middle\""
  else if (tolower($col) ~ "f_replace" && tolower($col) ~ "t_replace")
    $col = "\"Junior/Senior\""
  else if (tolower($col) ~ "s_replace" && tolower($col) ~ "t_replace")
    $col = "\"Middle/Senior\""
  else if (tolower($col) ~ "junior")
    $col = "\"Junior\""
  else if (tolower($col) ~ "s_replace")
    $col = "\"Middle\""
  else if (tolower($col) ~ "t_replace")
    $col = "\"Senior\""
  else
    $col = "\"-"
    print $0
}'
}

echo $str > $FILE_NAME

cat < $1 | while read -r; do cleaner >> $FILE_NAME; done


