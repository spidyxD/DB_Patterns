connect user1/user1;
drop table tprueba1;
connect user2/user2;
drop table tprueba2;
connect user3/user3;
drop table tprueba3;
connect system/manager as sysdba;
drop user user1;
drop user user2;
drop user user3;
commit;

exit;

SET LINESIZE 32000;
SET PAGESIZE 40000;
SET LONG 50000;