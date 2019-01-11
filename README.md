# DB_Patterns
<image src="presentation.jpg" alt="image not avaible"><br>
 <image src="presentation2.jpg" alt="image not avaible"><br>
  <image src="presentation3.jpg" alt="image not avaible"><br>
   <image src="presentation4.jpg" alt="image not avaible"><br>
<p>
1- To use the logminer tool you must have activated the archive mode in the database and also have established
the archives that will be used for the analysis in case of not using the archives can be used directly the log files.
2- The archive mode must be triggered in the database,
 later the archive you want will be selected this can be a single file where your location will be established or several
manually selected archives or establishing a range of dates.
3- Establish a data dictionary when logging into logminer, which will be used to extract
the information of the archives, this data dictionary can be created from the redo log files of the base of
data or select the online dictionary by default.
4- Once created the view v$logmnr_contents with the data obtained from logminer will be used
external software to perform the pattern analysis.
5- The software will allow to automate some of the processes for the creation of the logminer table, once the data has been obtained
you can make queries to the system to search for desired patterns of the records obtained by logminer, for this you can establish filters
the queries that allow to show precise information.
6- The software will show the results in the form of graphics, which will facilitate the understanding of the results
obtained from queries with filters that are made.
Some of the filters that can be done in the queries are:
Username transactions
Time Transactions
Table_name Transaction
Tablespace_name Transactions
Date Transactions
Operations
General View 
7- With this information obtained you will be able to find patterns in the transactions made by the users, which will allow to find
possible anomalies in the database.

</p>
