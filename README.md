# DB_Patterns
<image src="presentation.jpg" alt="image not avaible"><br>
 <image src="presentation2.jpg" alt="image not avaible"><br>
  <image src="presentation3.jpg" alt="image not avaible"><br>
   <image src="presentation4.jpg" alt="image not avaible"><br>
<p>
 The Forensic Analysis of Transactions model with LogMiner tool <br>

OBJECTIVE <br>

Analyzing utilities of the LogMiner tool  and log files structure , in order to detect anomalies in patterns into the database transactions, using the records of Oracle DBMS.<br>

RESULTS <br>


Steps <br>
1 Put the database in archive mode:<br>

2 Select an archive log file, where the transactions are located or stablish a range of time for select the archive files in that period:<br>

3 Create a select query and choose a filter for find the information you want for example:<br>

Some filters:<br>
Username transactions<br>
Time Transactions<br>
Table_name Transaction <br>
Tablespace_name Transactions<br>
Date Transactions<br>
Operations <br>
General View<br>



 
1- To use the logminer tool you must have activated the archive mode in the database and also have established
the archives that will be used for the analysis in case of not using the archives can be used directly the log files.<br>
2- The archive mode must be triggered in the database,
 later the archive you want will be selected this can be a single file where your location will be established or several
manually selected archives or establishing a range of dates.<br>
3- Establish a data dictionary when logging into logminer, which will be used to extract
the information of the archives, this data dictionary can be created from the redo log files of the base of
data or select the online dictionary by default.<br>
4- Once created the view v$logmnr_contents with the data obtained from logminer will be used
external software to perform the pattern analysis.<br>
5- The software will allow to automate some of the processes for the creation of the logminer table, once the data has been obtained
you can make queries to the system to search for desired patterns of the records obtained by logminer, for this you can establish filters
the queries that allow to show precise information.<br>
6- The software will show the results in the form of graphics, which will facilitate the understanding of the results
obtained from queries with filters that are made.<br>
Some of the filters that can be done in the queries are:<br>
Username transactions<br>
Time Transactions<br>
Table_name Transaction<br>
Tablespace_name Transactions<br>
Date Transactions<br>
Operations<br>
General View <br>
7- With this information obtained you will be able to find patterns in the transactions made by the users, which will allow to find
possible anomalies in the database.<br>
CONCLUSIONS<br>

When we are working with the logminer tool it is possible make an analysis in a simple way of the actions that are executed into database.<br>
That allow be able to see patterns as a result of traceability of transactions into data base that are record into the archive files that were selected.<br>

The advantages of archive mode are:<br>
 .Uselful for restore or recovering data base.<br>
 .Making an analysis of data base transactions with the log files for the monitoring activities of users.<br>
</p>
