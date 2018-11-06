BEGIN{
	RS ="%"
	FS ="$"
	delete users[0]
	delete operations[0]
	delete tablenames[0]
	delete tablespaces[0]
	delete owners[0]
	delete dates[0]
	delete times[0]
	delete sqls[0]
	delete sqls_1[0]
}
{
	#i = 1
	#split($0,record,"$")
	#users[length(users)+1] = record[i++]
	#operations[length(operations)+1] = record[i++]
	#tablenames[length(tablenames)+1] = record[i++]
	#tablespaces[length(tablespaces)+1] = record[i++]
	#owners[length(owners)+1] = record[i++]
	#dates[length(dates)+1] = record[i++]
	#times[length(times)+1] = record[i++]
	#sqls[length(sqls)+1] = record[i++]
	#sqls_1[length(sqls_1)+1] = record[i++]
	print NR")",$0
	
}
END{
	#print " USERNAME $ OPERATION $ TABLE_NAME $ TABLE_SPACE $ SEG_OWNER $ DATE $ TIME $ SQL $ SQL-1 "
	#for(i=1;i<length(sqls)-1;i++){
	#	print users[i]"$", operations[i]"$", tablenames[i]"$", tablespaces[i]"$", owners[i]"$", dates[i]"$", times[i]"$", sqls[i]"$", sqls_1[i]
	#}
}
