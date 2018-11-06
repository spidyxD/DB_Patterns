BEGIN{
	RS ="%"
	FS ="\r\n"
	delete users[0]
	delete dates[0]
	delete times[0]
	delete sqls[0][0]
	sql = ""
	redo = ""
	undo = ""
}
{
	#print "NR:", NR
	#print $0
	for(i=1;i<=NF;i++){
		#print i")", $i
		if($i~/^SQL>/){
			##print "sentence:", $i
			continue
		}
		if($i~/.* *[0-9]*\//){
			split($i,a," ")
			##print "user:",a[1]
			##print "date:",a[2]
			##print "time:",a[3]
			users[length(users)+1]=a[1]
			dates[length(dates)+1]=a[2]
			times[length(times)+1]=a[3]
		} else{
			sql = sprintf("%s %s",sql,$i)
		}
		if($i~/;/){
			##print "sql:", sql
			if(redo == ""){
				redo = sql
			}else if(undo == ""){
				undo = sql
			}
			sql = ""
		}
	}
	sqls[length(sqls)+1][1]=redo
	sqls[length(sqls)][2]=undo
	redo = ""
	undo = ""
}

END{
	#print "users len:", length(users)
	#print "dates len:", length(dates)
	#print "times len:", length(times)
	#print "sqls len:", length(sqls)
	print "USER%DATE%TIME%SQL%SQL-1"
	for(i=1;i<=length(dates);i++){
		print users[i]"%", dates[i]"%", times[i]"%", sqls[i][1]"%",sqls[i][2]
	}

}