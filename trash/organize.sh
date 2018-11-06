#sed -i 's/\r//g' file

export INPUT_FILE=data/unstructured.txt
export OUTPUT_FILE=data/structured.csv
export FORMAT_FILE=src/format.awk

echo "reading" $INPUT_FILE
echo "replacing %+ for % in" $INPUT_FILE
echo "applying" $FORMAT_FILE "to" $INPUT_FILE
echo "writing to"$OUTPUT_FILE

#cat $INPUT_FILE

cat $INPUT_FILE | awk '!/%/{print $0} /%+/{print "%"}' | awk -f $FORMAT_FILE > $OUTPUT_FILE
