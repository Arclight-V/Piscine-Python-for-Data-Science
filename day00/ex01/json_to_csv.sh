#!/bin/sh
SETCOLOR_FAILURE="echo \\033[1;31m"
SETCOLOR_NORMAL="echo \\033[0;39m"
SETCOLOR_EXAMPLE="echo \\033[1;32m"


if  [ ! $1 ] || [ ! $2 ] || [ ! $3 ] ; then
${SETCOLOR_FAILURE}
echo "FAILURE!!!";
${SETCOLOR_NORMAL}
echo "\$1 - filter.jq
\$2 - hh.json
\$3 - hh.csv"
${SETCOLOR_EXAMPLE}
echo "EXAMPLE"
${SETCOLOR_NORMAL}
echo "sh json_to_csv.sh filter.jq hh.json hh.csv\\n ";
    exit 1;
fi;


filter_str=$(<$1)

first_part="[$filter_str], (.items[] |"
second_part=" [."
last_part="]) | @csv"

IFS=", " read -ra ADDR <<< "$filter_str"
for i in "${ADDR[@]}"; do
    s="${i:1}"
    s=${s%?}
    second_part+="$s, ."
done

second_part=${second_part%???}

# jq: error: syntax error, unexpected INVALID_CHARACTER, expecting $end (Unix shell quoting issues?) at <top-level>, line 1:
#‘["id",
# jq: 1 compile error
#
# full_comand="'"$first_part$second_part$last_part"'"
# echo "jq -r $full_comand $2 > $3";
# jq -r $full_comand $2 > $3

full_comand=$first_part$second_part$last_part

echo $full_comand > "tmp.txt"
jq -rf "tmp.txt" $2 > $3
rm tmp.txt

