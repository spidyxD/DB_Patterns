--conn sys/k1n9r4d2 as sysdba;
--@C:\Users\Addiel\Desktop\logminerTools.sql;
drop table logminerFiltered;
SELECT SUPPLEMENTAL_LOG_DATA_MIN FROM V$DATABASE;

ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;--

SELECT SUPPLEMENTAL_LOG_DATA_MIN FROM V$DATABASE;

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_06\O1_MF_1_9_FY3GZX1J_.ARC', -
       OPTIONS => DBMS_LOGMNR.NEW);

--EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   --LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_05\O1_MF_1_11_FY2111C4_.ARC');

EXECUTE DBMS_LOGMNR.START_LOGMNR(OPTIONS => DBMS_LOGMNR.DICT_FROM_ONLINE_CATALOG);

SELECT USERNAME, OPERATION, TABLE_NAME, TABLE_SPACE, SEG_OWNER, TIMESTAMP as date_, (XIDUSN || ':' || XIDSLT || ':' || XIDSQN) AS time_, SQL_REDO, sql_undo 
        FROM V$LOGMNR_CONTENTS 
        WHERE username <> 'UNKNOWN' 
        and username <> 'SYS' 
        and table_space <> 'None' 
        and table_space <> 'UNKNOW' 
        and table_name <> 'None';

create table logminerFiltered(
    username varchar2(30),
    operation varchar2(32),
    table_name varchar2(32),
    table_space varchar2(32),
    seg_owner varchar2(32),
    date_ varchar(250),
    time_ varchar(250),
    sql_ varchar2(4000),
    sql_1 varchar2(4000)
);


CREATE OR REPLACE PROCEDURE filting_logs 
IS
  CURSOR cur IS SELECT USERNAME, OPERATION, TABLE_NAME, TABLE_SPACE, SEG_OWNER, TIMESTAMP as date_, (XIDUSN || ':' || XIDSLT || ':' || XIDSQN) AS time_, SQL_REDO, sql_undo 
                        FROM V$LOGMNR_CONTENTS WHERE OPERATION IS NOT NULL;
  username varchar2(30);
  operation varchar2(32);
  table_name varchar2(32);
  table_space varchar2(32);
  seg_owner varchar2(32);
  date_ varchar(250);
  time_ varchar(250);
  sql_ varchar2(4000);
  sql_1 varchar2(4000);
BEGIN
    OPEN cur;
    FETCH cur INTO username, operation, table_name, table_space, seg_owner, date_, time_, sql_, sql_1;
    WHILE cur % FOUND LOOP
        insert into logminerFiltered values(username, operation, table_name, table_space, seg_owner, date_, time_, sql_, sql_1);
        FETCH cur INTO username, operation, table_name, table_space, seg_owner, date_, time_, sql_, sql_1;
    END LOOP;
    commit;
    CLOSE cur;
END;
/
show errors;

exec filting_logs

--select * from logminerFiltered where username <> 'UNKNOWN' and
--    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None';